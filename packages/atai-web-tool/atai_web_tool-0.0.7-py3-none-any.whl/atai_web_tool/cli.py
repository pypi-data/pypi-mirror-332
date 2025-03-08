import argparse
import asyncio
import sys
import random
from playwright.async_api import async_playwright
from readability import Document
from bs4 import BeautifulSoup
from atai_web_tool.user_agents import USER_AGENTS


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

async def extract_content(url: str, headless: bool, no_sandbox: bool) -> str:
    async with async_playwright() as p:
        args = ["--no-sandbox"] if no_sandbox else []
        browser = await p.chromium.launch(headless=headless, args=args)
        
        # Create a context with a realistic user agent
        random_user_agent = random.choice(USER_AGENTS)
        context = await browser.new_context(
            user_agent=random_user_agent
        )
        page = await context.new_page()

        # Only block images and fonts, allow JavaScript and stylesheets
        await page.route("**/*.{png,jpg,jpeg,gif,webp,svg}", lambda route: route.abort())
        await page.route("**/*.{woff,woff2,ttf,otf,eot}", lambda route: route.abort())

        try:
            # Navigate to the URL and wait until network is idle (most resources loaded)
            await page.goto(url, wait_until="networkidle", timeout=30000)
            
            # Additional wait to allow JavaScript to execute
            await page.wait_for_timeout(2000)
            
            # Get the content properly with await
            html_content = await page.content()
            
            # Check if we need to bypass any protection
            if "Enable JavaScript and cookies to continue" in html_content:
                # Try to find and click any "Continue" buttons
                try:
                    await page.click('text="Continue"', timeout=3000)
                    await page.wait_for_timeout(2000)
                    # Get updated content after clicking
                    html_content = await page.content()
                except:
                    pass
            
            # Use readability-lxml to extract the main content HTML
            doc = Document(html_content)
            main_html = doc.summary()
            
            # Clean the HTML to get plain text
            soup = BeautifulSoup(main_html, "html.parser")
            main_text = soup.get_text(separator="\n", strip=True)
            
            return main_text
        
        finally:
            await browser.close()

def main():
    parser = argparse.ArgumentParser(
        description="Extract the main content from a webpage using Playwright, readability-lxml, and BeautifulSoup."
    )
    parser.add_argument("url", help="The URL of the webpage to extract content from.")
    parser.add_argument(
        "--no-sandbox",
        action="store_true",
        help="Run browser with no sandbox (useful when running as root or in restricted environments)."
    )
    parser.add_argument(
        "--headless",
        type=str2bool,
        nargs='?',
        const=True,
        default=True,
        help="Run browser in headless mode (default: True). Use '--headless false' to disable headless mode."
    )
    args = parser.parse_args()

    try:
        content = asyncio.run(extract_content(args.url, args.headless, args.no_sandbox))
        print(content)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

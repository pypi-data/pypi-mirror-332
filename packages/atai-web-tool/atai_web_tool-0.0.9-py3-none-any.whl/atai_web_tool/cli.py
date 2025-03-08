import argparse
import asyncio
import sys
import random
from playwright.async_api import async_playwright
from readability import Document
from bs4 import BeautifulSoup
from atai_web_tool.user_agents import USER_AGENTS
import newspaper

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def extract_with_newspaper(url: str) -> str:
    try:
        # Create an article instance and download it
        article = newspaper.article(url)
        article.download()
        article.parse()
        content = article.text.strip()
        if content and len(content) > 150:
            return content
    except Exception as e:
        # Optionally log the exception e
        pass
    return ""

async def extract_with_playwright(url: str, headless: bool, no_sandbox: bool) -> str:
    async with async_playwright() as p:
        args = ["--no-sandbox"] if no_sandbox else []
        browser = await p.chromium.launch(headless=headless, args=args)
        
        # Create a context with a realistic user agent
        random_user_agent = random.choice(USER_AGENTS)
        context = await browser.new_context(user_agent=random_user_agent)
        page = await context.new_page()

        # Block images and fonts
        await page.route("**/*.{png,jpg,jpeg,gif,webp,svg}", lambda route: route.abort())
        await page.route("**/*.{woff,woff2,ttf,otf,eot}", lambda route: route.abort())

        try:
            # Navigate to the URL and wait until the page loads
            await page.goto(url, wait_until="load", timeout=60000)
            await page.wait_for_timeout(2000)
            html_content = await page.content()
            
            # Handle any potential protection pages
            if "Enable JavaScript and cookies to continue" in html_content:
                try:
                    # await page.click('text="Continue"', timeout=3000)
                    await page.wait_for_timeout(2000)
                    html_content = await page.content()
                except:
                    pass
            
            # Use readability-lxml to extract the main HTML content
            doc = Document(html_content)
            main_html = doc.summary()
            
            # Clean the HTML to get plain text
            soup = BeautifulSoup(main_html, "html.parser")
            main_text = soup.get_text(separator="\n", strip=True)
            return main_text
        
        finally:
            await browser.close()

async def extract_content(url: str, headless: bool, no_sandbox: bool) -> str:
    # First attempt using Newspaper4k in a separate thread
    newspaper_content = await asyncio.to_thread(extract_with_newspaper, url)
    if newspaper_content:
        return newspaper_content
    # If Newspaper4k extraction fails, fall back to using Playwright
    return await extract_with_playwright(url, headless, no_sandbox)

def main():
    parser = argparse.ArgumentParser(
        description="Extract the main content from a webpage using Newspaper4k (primary) and Playwright as fallback."
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

from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        try:
            page = await browser.new_page()
            await page.goto("https://facebook.com")
            print(page.title())
            # your code here
        finally:
            await browser.close()

import asyncio
asyncio.run(run())
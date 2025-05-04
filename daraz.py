from playwright.sync_api import sync_playwright
import time

def test_daraz_search():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Go to Daraz Bangladesh
        page.goto("https://www.daraz.com.bd")

        # Close popup banner if appears
        try:
            page.locator('button[aria-label="close banner"]').click(timeout=3000)
        except:
            print("No banner popup to close")

        # Accept cookies if popup appears
        try:
            page.get_by_text("ACCEPT ALL COOKIES").click(timeout=3000)
        except:
            print("No cookie popup to accept")

        # Fill search box with "laptop"
        page.fill('input[name="q"]', 'laptop')

        # Press Enter to search
        page.keyboard.press('Enter')

        # Wait for search results to load
        try:
            page.wait_for_selector('.c16H9d', timeout=10000)
            print("✅ Search results loaded")
        except:
            print("❌ Search results not found")

        # Screenshot for proof
        page.screenshot(path="daraz_search_result.png")

        # Close browser
        browser.close()

# 🔥 This part must be at the bottom to make it run directly
if __name__ == "__main__":
    test_daraz_search()

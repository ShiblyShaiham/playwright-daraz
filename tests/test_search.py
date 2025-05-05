import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from playwright.sync_api import sync_playwright
from pages.home_page import HomePage

def test_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        home = HomePage(page)
        home.open()
        home.close_popups()
        home.search_product("laptop")

        page.wait_for_selector(".c16H9d", timeout=10000)
        page.screenshot(path="daraz_search.png")
        browser.close()

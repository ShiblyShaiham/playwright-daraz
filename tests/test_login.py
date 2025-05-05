# tests/test_login.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login = LoginPage(page)
        login.go_to_login()
        login.login("your_email@example.com", "your_password")  # ❗ Replace with real or dummy creds

        # Example: check if user is logged in (adapt based on real element)
        assert "Logout" in page.content()

        browser.close()

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')
    select_dropdown=page.query_selector('//input[@value="FeMale"]')
    select_dropdown.check()
    page.wait_for_timeout(3000)
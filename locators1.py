from pydoc import pager

from playwright.sync_api import sync_playwright
with sync_playwright() as play:
    browser=play.chromium.launch(headless=False)
    page =browser.new_page()
    page.goto("https://demo.automationtesting.in/")

    #cssselector id,class,attribute
    #idusing
    emailtxtbox=page.wait_for_selector('#email')
    emailtxtbox.type('test@gmail.com')
    buttonlogin=page.wait_for_selector('#enter')
    buttonlogin.click()
    page.wait_for_timeout(3000)
      

# pages/login_page.py

class LoginPage:
    def __init__(self, page):
        self.page = page

    def go_to_login(self):
        self.page.goto("https://www.daraz.com.bd")
        self.page.click("text=Login")

    def login(self, email, password):
        self.page.fill('input[type="text"]', email)
        self.page.fill('input[type="password"]', password)
        self.page.click('button[type="submit"]')

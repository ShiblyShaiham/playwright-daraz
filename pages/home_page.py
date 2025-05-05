class HomePage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://www.daraz.com.bd")

    def close_popups(self):
        try:
            self.page.locator('button[aria-label="close banner"]').click(timeout=3000)
        except:
            pass
        try:
            self.page.get_by_text("ACCEPT ALL COOKIES").click(timeout=3000)
        except:
            pass

    def search_product(self, keyword):
        self.page.fill('input[name="q"]', keyword)
        self.page.keyboard.press("Enter")

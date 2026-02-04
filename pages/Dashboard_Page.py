class DashboardPage:

    def __init__(self, page):
        self.page = page

    def click_logout(self):
        self.page.click("a[href='/logout']")
class DashboardPage:

    def __init__(self, page):
        self.page = page

    def click_logout(self):
        with self.page.expect_navigation():
            self.page.get_by_role("link", name="Logout").click()

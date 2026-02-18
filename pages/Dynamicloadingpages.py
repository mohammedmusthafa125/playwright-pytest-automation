class DynamicLoadingPage:
    def __init__(self,page):
        self.page = page
        self.start_button=page.get_by_role("button",name="Start")
        self.finish_text=page.locator("#finish")

    def open(self):
        self.page.goto("dynamic_loading/2")

    def load(self):
        self.start_button.click()

    def get_finish_text(self):
        self.finish_text.wait_for()
        return self.finish_text.inner_text()
# class LoginPage:
#     def __init__(self, page):
#         self.page = page
#
#     def open(self):
#         self.page.goto("https://the-internet.herokuapp.com/login")
#
#     def login(self, username, password):
#         self.page.fill("#username", username)
#         self.page.fill("#password", password)
#
#         with self.page.expect_navigation():
#             self.page.click("button[type='submit']")
#     def get_flash_message(self):
#         flash = self.page.locator("#flash")
#         flash.wait_for() # it will keep waiting so that return does gives nonne value
#
#         return flash.inner_text() #safer practice than text_content

#data driven testing
from utils.config import Config

class LoginPage:
    def __init__(self,page):
        self.page=page

        self.username_input=page.locator("#username")
        self.password_input=page.locator("#password")
        self.login_button=page.locator("button[type='submit']")
        self.flash_message=page.locator("#flash")

    def open(self):
        self.page.goto(
            Config.BASE_URL +Config.LOGIN_PATH,
            wait_until="domcontentloaded",
            timeout=60000
        )

    def login(self,username,password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_flash_message(self):
        flash = self.page.locator("#flash")
        flash.wait_for()
        return flash.inner_text().replace("×", "").strip()

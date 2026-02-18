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

    def open(self):
        self.page.goto(Config.BASE_URL + Config.LOGIN_PATH)

    def test_login(page, config):
        page.goto(f"{config['base_url']}/login")
        page.fill("#username", config["username"])
        page.fill("#password", config["password"])
        page.click("button[type='submit']")

    def get_flash_message(self):
        flash = self.page.locator("#flash")
        flash.wait_for()
        return flash.inner_text().replace("×", "").strip()

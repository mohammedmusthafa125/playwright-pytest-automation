# import pytest
# from pages.Login_Page import LoginPage
#
# @pytest.mark.parametrize("username,password,expected", [
#     ("tomsmith", "SuperSecretPassword!", "success"),
#     ("wrong", "wrong", "failure")
# ])
# def test_login(page, username, password, expected):
#     login = LoginPage(page)
#     login.open()
#     login.login(username, password)
#
#     message = login.get_flash_message()
#
#     if expected == "success":
#         assert "You logged into a secure area!" in message
#     else:
#         assert "Your username is invalid!" in message


import pytest

from pages.Login_Page import LoginPage
from testdata.login_data import login_test_data

@pytest.mark.parametrize("data", login_test_data)
def test_login(page,data):
    login=LoginPage(page)
    login.open()
    login.login(data["username"], data["password"])

    message=login.get_flash_message()
    if data["expected"] == "success":
        assert "You logged into a secure area!" in message
    else:
        assert "Your username is invalid!" in message
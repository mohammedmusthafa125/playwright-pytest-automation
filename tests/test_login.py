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
from testdata.login_data import negative_login_data

@pytest.mark.smoke
@pytest.mark.parametrize("data", login_test_data)
def test_login(page,data):
    login=LoginPage(page)
    login.open()
    login.login(data["username"], data["password"])

    message=login.get_flash_message()
   # assert False
    if data["expected"] == "success":
        assert message == "You logged into a secure area!"
    else:
        assert message == "Your username is invalid!"

@pytest.mark.regression
@pytest.mark.parametrize("data", negative_login_data)
def test_invalid_login(page, data):
    login = LoginPage(page)
    login.open()
    login.login(data["username"], data["password"])

    message = login.get_flash_message()
    assert message == data["expected"]




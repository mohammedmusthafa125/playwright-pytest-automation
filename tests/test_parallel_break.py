import pytest
import time

@pytest.fixture(scope="session")
def shared_user():
    return {"username": "tomsmith", "password": "SuperSecretPassword!"}


def test_login(shared_user, page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", shared_user["username"])
    page.fill("#password", shared_user["password"])
    page.click("button[type='submit']")
    assert page.locator("text=Secure Area").is_visible()


def test_logout(shared_user, page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", shared_user["username"])
    page.fill("#password", shared_user["password"])
    page.click("button[type='submit']")

    page.click("text=Logout")
    time.sleep(2)


import pytest
from playwright.sync_api import sync_playwright
import os
from datetime import datetime

@pytest.fixture
def page(env):

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(base_url=env["base_url"])
        page = context.new_page()
        yield page
        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)
        if page:
            os.makedirs("screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_name = f"{item.name}_{timestamp}.png"
            page.screenshot(path=f"screenshots/{screenshot_name}")

from pages.Login_Page import LoginPage


@pytest.fixture
def logged_in_page(page):
    login =LoginPage(page)
    login.open()
    login.login("tomsmith","SuperSecretPassword!")
    return page

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment to run tests against"
    )


import pytest
from config.environments import ENVIRONMENTS

@pytest.fixture(scope="session")
def env(request):
    selected_env = request.config.getoption("--env")
    return ENVIRONMENTS[selected_env]


@pytest.fixture(scope="session")
def shared_user():
    return {"username": "paralleluser", "password": "Test123"}


from dotenv import load_dotenv
import os

load_dotenv()
@pytest.fixture(scope="session")

def config():
    return{
        "base_url":os.getenv("BASE_URL"),
        "username":os.getenv("USERNAME"),
        "password":os.getenv("PASSWORD"),

    }

import pytest
from playwright.sync_api import sync_playwright
import os
from datetime import datetime

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])

        context = browser.new_context()
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
import pytest
from playwright.sync_api import sync_playwright
from utils.config import Config

import pytest
from playwright.sync_api import sync_playwright
from utils.config import Config

@pytest.fixture
def page():
    with sync_playwright() as p:

        if Config.BROWSER == "chromium":
            browser = p.chromium.launch(headless=Config.HEADLESS)
        elif Config.BROWSER == "firefox":
            browser = p.firefox.launch(headless=Config.HEADLESS)
        else:
            browser = p.webkit.launch(headless=Config.HEADLESS)

        page = browser.new_page()
        yield page
        browser.close()


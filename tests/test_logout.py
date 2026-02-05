import pytest

from pages.Login_Page import LoginPage
from pages.Dashboard_Page import DashboardPage

@pytest.mark.regression
def test_logout(logged_in_page):
    dashboard = DashboardPage(logged_in_page)
    dashboard.click_logout()

    assert "login" in logged_in_page.url
    assert False



import pytest

from pages.Login_Page import LoginPage
from pages.Dashboard_Page import DashboardPage

@pytest.mark.regression
def test_logout(logged_in_page):
    dashboard = DashboardPage(logged_in_page)

    dashboard.click_logout()



    assert dashboard.page.get_by_text("You logged out").is_visible()





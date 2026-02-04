from pages.Login_Page import LoginPage
from pages.Dashboard_Page import DashboardPage

def test_logout(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.open()
    login.login("tomsmith", "SuperSecretPassword!")

    dashboard.click_logout()

    assert "login" in page.url

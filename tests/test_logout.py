from main.pages.dashboard_page import DashboardPage
from main.pages.login_page import LoginPage
from test_data.login_data import LoginData
from utils import verify


class TestLogout:
    def test_positive_logout(self):
        login_data = LoginData()
        login_page = LoginPage().open()
        login_page.login(username=login_data.username, password=login_data.password)

        dashboard_page = DashboardPage()
        verify(
            check=dashboard_page.is_loaded(),
            f_msg="Wrong page is opened",
            p_msg="DashboardPage is opened"
        )

        dashboard_page.header.logout()
        verify(
            check=login_page.is_loaded(),
            f_msg="Wrong page is opened",
            p_msg="LoginPage is opened"
        )



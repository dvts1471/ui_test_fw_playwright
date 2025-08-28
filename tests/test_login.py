from main.pages.dashboard_page import DashboardPage
from main.pages.login_page import LoginPage
from test_data.login_data import LoginData
from utils import verify


class TestLogin:

    def test_positive_login(self):
        login_data = LoginData()
        login_page = LoginPage().open()
        login_page.login(username=login_data.username, password=login_data.password)

        dashboard_page = DashboardPage()
        dashboard_page.is_loaded()
        current_url = dashboard_page.get_current_url()
        verify(
            check=[
                dashboard_page.is_loaded(),
                current_url == dashboard_page.url
            ],
            f_msg=f'The wrong page is opened {current_url}',
            p_msg="DashboardPage is opened"
        )


    def test_empty_login(self):
        login_data = LoginData(username="", password="")

        login_page = LoginPage().open()
        login_page.login(username=login_data.username, password=login_data.password)

        current_url = login_page.get_current_url()
        verify(
            check=current_url == login_page.url,
            f_msg=f'The wrong page is opened {current_url}',
            p_msg="LoginPage is opened"
        )


        verify(
            check=login_page.username_validation_msg.get_text() == 'Required',
            f_msg='Wrong validation message for username',
            p_msg="Right validation message for username"
        )
        verify(
            check=login_page.password_validation_msg.get_text() == 'Required',
            f_msg='Wrong validation message for password',
            p_msg="Right validation message for password"
        )

    def test_invalid_pass(self):
        login_data = LoginData(password='invalid')

        login_page = LoginPage().open()
        login_page.login(username=login_data.username, password=login_data.password)

        verify(
            check=login_page.alert.get_text() == "Invalid credentials",
            f_msg="Wrong alert message",
            p_msg="Right alert message"
        )
from tabnanny import check

from main.pages.admin_add_user_page import AdminAddUserPage
from main.pages.admin_page import AdminPage
from main.pages.dashboard_page import DashboardPage
from main.pages.login_page import LoginPage
from test_data.login_data import LoginData
from utils import verify


class TestAdmin:
    def test_add_user(self):
        login_data = LoginData()
        login_page = LoginPage().open()
        login_page.login(username=login_data.username, password=login_data.password)

        dashboard_page = DashboardPage()

        dashboard_page.side_menu.admin_item.click()

        current_url = dashboard_page.get_current_url()
        admin_page = AdminPage()

        verify(
            check=[
                current_url==admin_page.url,
                admin_page.is_loaded()
            ],
            f_msg=f'The wrong page is opened {current_url}',
            p_msg="AdminPage is opened"
        )

        admin_page.add_user_button.click()
        admin_add_user_page = AdminAddUserPage()
        admin_add_user_page.is_loaded()


        current_url = dashboard_page.get_current_url()
        verify(
            check=admin_add_user_page.add_user_title.is_visible(),
            f_msg=f'The wrong page is opened {current_url}',
            p_msg="AdminAddUserPage is opened"
        )

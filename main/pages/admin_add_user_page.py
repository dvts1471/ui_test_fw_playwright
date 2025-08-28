from constants import URL
from core.elements import BaseElement
from core.elements.button import Button
from core.pages import BasePage
from main.components.dashboard.my_actions import MyActions
from main.components.dashboard.time_at_work_component import TimeAtWorkComponent
from main.components.header import Header
from main.components.side_menu import SideMenu


class AdminAddUserPage(BasePage):
    url = f"{URL}/admin/saveSystemUser"

    header = Header()
    side_menu = SideMenu()

    add_user_title = BaseElement(locator='//h6[contains(., "Add User")]')

    def is_loaded(self, timeout=5):
        return self.add_user_title.wait_element_visible(timeout=timeout)



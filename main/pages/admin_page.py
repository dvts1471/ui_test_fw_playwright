from constants import URL
from core.elements.button import Button
from core.pages import BasePage
from main.components.dashboard.my_actions import MyActions
from main.components.dashboard.time_at_work_component import TimeAtWorkComponent
from main.components.header import Header
from main.components.side_menu import SideMenu


class AdminPage(BasePage):
    url = f"{URL}/admin/viewSystemUsers"

    header = Header()
    side_menu = SideMenu()

    add_user_button = Button(locator='//button[contains(., "Add")]')

    def is_loaded(self, timeout=5):
        return self.add_user_button.wait_element_visible(timeout=timeout)


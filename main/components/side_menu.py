from core.components import BaseComponent
from core.elements.button import Button
from core.elements.input import Input


class SideMenu(BaseComponent):
    locator = '//*[@aria-label="Sidepanel"]'
    search_input = Input(locator=f'{locator}//*[contains(@placeholder, "Search")]')
    dashboard_item = Button(locator=f'{locator}//*[contains(@placeholder, "Dashboard")]')
    admin_item = Button(locator=f'{locator}//a[contains(., "Admin")]')

    def __init__(self):
        super().__init__(self.locator)

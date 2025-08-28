from core.components import BaseComponent
from core.elements import BaseElement
from core.elements.button import Button
from main.components.header.user_dropdown import UserDropdown


class Header(BaseComponent):
    locator = '//header'

    title = BaseElement(locator=f"{locator}//h6")
    upgrade_button = Button(locator=f'{locator}//button[contains(.,"Upgrade")]')
    user_dropdown = UserDropdown()

    def __init__(self):
        super().__init__(self.locator)

    def logout(self):
        self.logger.info("Logging out")
        self.user_dropdown.logout()


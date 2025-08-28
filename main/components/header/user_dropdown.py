from core.components import BaseComponent
from core.elements.button import Button


class UserDropdown(BaseComponent):
    locator = '//*[@class="oxd-userdropdown-tab"]'

    def __init__(self):
        super().__init__(self.locator)

    about_item = Button(locator=f'//*[{locator}]/a[contains(., "About")]')
    support_item = Button(locator=f'//*[{locator}]/a[contains(., "Support")]')
    change_password_item = Button(locator=f'//*[{locator}]/a[contains(., "Change Password")]')
    logout_item = Button(locator=f'//*[{locator}]/a[contains(., "Logout")]')

    def logout(self):
        self.element.click()
        self.logout_item.click()
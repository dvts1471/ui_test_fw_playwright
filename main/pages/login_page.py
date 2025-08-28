from constants import URL
from core.elements import BaseElement
from core.elements.button import Button
from core.elements.input import Input
from core.pages import BasePage


class LoginPage(BasePage):
    url = f"{URL}/auth/login"

    login_title = BaseElement(locator='//h5[contains(., "Login")]')

    username_input = Input(locator='//*[@name="username"]')
    username_validation_msg = BaseElement(locator=f'//*[.{username_input.locator}]/span')

    password_input = Input(locator='//*[@name="password"]')
    password_validation_msg = BaseElement(locator=f'//*[.{password_input.locator}]/span')

    login_button = Button(locator='//*[@type="submit"]')

    alert = BaseElement(locator='//*[@role="alert"]')

    def login(self, username, password):
        self.logger.info(f'Login with username: "{username}" password: "{password}"')
        self.username_input.fill(username)
        self.password_input.fill(password)

        self.login_button.click()

    def is_loaded(self, timeout=5):
        return all([
            self.login_title.wait_element_visible(timeout=timeout)
        ])
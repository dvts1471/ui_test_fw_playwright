import re
from asyncio import timeout
from venv import logger

from playwright.sync_api import Locator

from utils import get_utc_now, is_timeout_reached
from utils.logger import Logger
from utils.playwright_browser_manager import PlaywrightBrowserManager


class BaseElement:
    WAIT_TIMEOUT_SEC = 10
    element_type = "base_element"

    def __init__(self, *args, locator=None, name=None, text=None, role=None, test_id=None):
        if args:
            raise ValueError(f"Invalid args were passed: {args}")
        self.logger = Logger(self.__class__.__name__)
        self.role = role
        self.name = name
        self.locator = locator
        self.test_id = test_id
        self.text = text
        if locator:
            self.logger.debug('Locator is defined. All other element search parameter will be ignored.')

    @property
    def page(self):
        return PlaywrightBrowserManager().get_page()

    def get_locator(self) -> Locator:
        if self.locator:
            return self.page.locator(self.locator)

        if self.name:
            element = self.page.get_by_role(self.role, name=self.name)
        else:
            element = self.page.get_by_role(self.role)

        if self.text:
            element = element.get_by_text(self.text)
        if self.test_id:
            element = element.get_by_test_id(self.test_id)

        return element

    @property
    def element(self) -> Locator:
        return self.get_locator()

    def get_text(self):
        return self.element.inner_text()

    def __repr__(self):
        locator = self.get_locator()
        selector = re.search(r'(?<=selector\=\').*(?=\')', str(locator)).group()
        return f"{self.__class__.__name__}: {selector}"

    def is_visible(self):
        return self.element.nth(0).is_visible()

    def hover(self):
        self.logger.debug(f"Hovering over element {self.element_type} with locator '{self.locator}'")
        self.element.hover()

    def verify_text(self, expected_value):
        actual_value = (
            self.get_text() if self.get_text() else self.get_attribute("value")
        )
        if actual_value != expected_value:
            raise AssertionError(
                f"Expected: {expected_value}, Actual: {actual_value}"
            )

    def wait_element_clickable(self, timeout=WAIT_TIMEOUT_SEC):
        start_time = get_utc_now()
        while not is_timeout_reached(start_time, timeout_sec=timeout):
            if self.element.is_visible() and not self.element.is_disabled():
                return self
            self.page.wait_for_timeout(0.5)
        error_msg = f'Error on waiting for {self.element_type} with locator "{self.locator}"'
        self,logger.error(error_msg)
        raise Exception(error_msg)

    def wait_element_visible(self, timeout=WAIT_TIMEOUT_SEC):
        start_time = get_utc_now()
        while not is_timeout_reached(start_time, timeout_sec=timeout):
            if self.element.is_visible():
                return self
            self.page.wait_for_timeout(0.5)
        error_msg = f'Error on waiting for {self.element_type} with locator "{self.locator}"'
        self,logger.error(error_msg)
        raise Exception(error_msg)

    def is_clickable(self, timeout=5):
        try:
            self.wait_element_clickable(timeout=timeout)
            self.logger.debug(f"Element {self.element_type} is clickable")
            return True
        except:
            self.logger.debug(f"Element {self.element_type} is not clickable")
            return False

    def click(self):
        try:
            self.element.click()
            self.logger.info(f'Clicked on {self.element_type} with locator "{self.locator}"!')
        except Exception as error:
            error_message = f'Error on clicking {self.element_type} with locator "{self.locator}"!'
            self.logger.error(error_message)
            raise error.__class__(error_message)
        return self

    def get_attribute(self, attribute):
        self.logger.debug(
            f"Getting attribute '{attribute}' from {self.element_type} '{self.locator}'"
        )
        return self.element.get_attribute(attribute)

    def get_property(self, property_name):
        self.logger.debug(
            f"Getting property '{property_name}' from {self.element_type} '{self.locator}'"
        )
        return self.element.evaluate(f"element => element.{property_name}")

    def get_child_element(self, locator):
        return self.element.locator(locator)
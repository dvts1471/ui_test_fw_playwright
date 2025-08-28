from abc import ABC
from asyncio import wait_for, timeout

from constants import URL
from utils import PlaywrightBrowserManager
from utils.logger import Logger


class BasePage(ABC):
    url = URL

    def __init__(self):
        self.logger = Logger(self.__class__.__name__)

    @property
    def page(self):
        return PlaywrightBrowserManager().get_page()

    def open(self):
        self.page.goto(url=self.url, wait_until="networkidle")
        self.page.wait_for_function("document.readyState === 'complete'")
        self.logger.info(f"Open {self.__class__.__name__}")
        return self

    def is_loaded(self, timeout=5):
        raise NotImplemented

    def get_current_url(self, timeout=5):
        self.page.wait_for_function("document.readyState === 'complete'")
        return self.page.evaluate("document.URL")

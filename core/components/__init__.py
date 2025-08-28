from abc import ABC
from core.elements import BaseElement
from utils import PlaywrightBrowserManager
from utils.logger import Logger


class BaseComponent(ABC, BaseElement):

    def __init__(self, locator):
        super().__init__(locator=locator)
        self.logger = Logger(self.__class__.__name__)

    @property
    def page(self):
        return PlaywrightBrowserManager().get_page()


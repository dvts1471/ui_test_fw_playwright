from playwright.sync_api import sync_playwright

from utils import Logger


class PlaywrightBrowserManager:
    __browser = None
    __context = None
    _page = None
    __playwright = None

    def __init__(self):
        self.logger = Logger(self.__class__.__name__)

    def is_page_initialized(self):
        """Check if page is initialized"""
        return self._page is not None

    @property
    def _playwright(self):
        if not self.__playwright:
            self.__class__.__playwright = sync_playwright().start()
        return self.__playwright

    @property
    def _browser(self):
        if not self.__browser:
            self.__class__.__browser = self._playwright.chromium.launch(
                headless=False
            )
        return self.__browser

    @property
    def _context(self):
        if not self.__context:
            self.__class__.__context = self._browser.new_context(
                ignore_https_errors=True
            )
        return self.__context

    def get_page(self):
        return self._page if self._page else self.create_page()

    def create_page(self):
        if self._page is not None:
            self.quit_page()
            self.logger.debug("Playwright page quit succeed")
        self.__class__._page = self._context.new_page()

        return self._page

    def quit_page(self):
        self.__context.close()
        self.__browser.close()
        self.__playwright.stop()
        self._page = None
        self.__context = None
        self.__browser = None
        self.__playwright = None
import pytest

from utils import PlaywrightBrowserManager


@pytest.fixture(autouse=True, scope="function")
def teardown():
    yield
    if PlaywrightBrowserManager().is_page_initialized():
        PlaywrightBrowserManager().quit_page()
import os
import re
import datetime
from pathlib import Path
from typing import Union, List

from utils.logger import Logger
from utils.playwright_browser_manager import PlaywrightBrowserManager

counter = 0

def get_current_test_name():
    test_full_name = os.environ.get('PYTEST_CURRENT_TEST')
    return re.search('::(\w+)\s', test_full_name).group(1)


def verify(check: Union[List[bool], bool], f_msg, p_msg=''):
    global counter
    page = PlaywrightBrowserManager().get_page()
    logger = Logger("Verification")
    if isinstance(check, bool):
        check = [check]
    assert all(check), f_msg
    evidence_path = Path(f"./test_results/evidences/{get_current_test_name()}/evidence_{counter}.png")
    if not evidence_path.parent.exists():
        evidence_path.parent.mkdir(parents=True)
    page.screenshot(path=evidence_path)
    counter += 1
    logger.info(f'Verified: {p_msg} ({evidence_path})')

def get_utc_now():
    return datetime.datetime.now(datetime.timezone.utc)

def is_timeout_reached(start_time, timeout_min=0, timeout_sec=0):
    now = get_utc_now()
    return now - start_time > datetime.timedelta(minutes=timeout_min, seconds=timeout_sec)


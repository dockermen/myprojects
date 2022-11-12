import time,os
import logging
from playwright.sync_api import Playwright, sync_playwright
from concurrent_log_handler import ConcurrentRotatingFileHandler
from playwright._impl._api_types import TimeoutError,Error


log = logging.getLogger()
rotateHandler = ConcurrentRotatingFileHandler('./2.log', "a", 1024*1024, 5,encoding='utf-8')
fmt = logging.Formatter('[%(levelname)s]: %(message)s')
rotateHandler.setFormatter(fmt)
log.addHandler(rotateHandler)
log.setLevel(logging.INFO)


with sync_playwright() as playwright:
    try:
        webkit = playwright.chromium.launch(headless=True)
        context = webkit.new_context()
        page = context.new_page()
        page.goto("https://www.baidu.com/")
        print(page.content())
        log.info(f"{page.content()}")
    except Exception as e:
        print(e)
    finally:
        time.sleep(10)
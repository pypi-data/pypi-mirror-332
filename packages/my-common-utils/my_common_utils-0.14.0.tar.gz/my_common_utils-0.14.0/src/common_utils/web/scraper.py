from dataclasses import dataclass
from typing import Literal
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

# from undetected_chromedriver.v2 import Chrome as UndetectedChrome

from common_utils.logger import create_logger


@dataclass
class DriverAction:
    action: Literal["url", "sleep", "click", "send_keys", "get_text", "get_texts"]
    identifier: str | None = None
    input: str | int | None = None



class SeleniumHandler:
    log = create_logger("SeleniumHandler")

    def __init__(self, headless: bool = True, undetected: bool = False, verbose: bool = False, raise_exceptions: bool = True):
        self.headless = headless
        self.undetected = undetected
        self.verbose = verbose
        self.raise_exceptions = raise_exceptions

    def log_msg(self, message: str, level: Literal["debug", "info", "warning", "error"] = "info"):
        if self.verbose is False:
            return
        match level:
            case "debug":
                self.log.debug(message)
            case "info":
                self.log.info(message)
            case "warning":
                self.log.warning(message)
            case "error":
                self.log.error(message)
            case _:
                self.log.info(message)

    def get_driver(self):
        if self.undetected:
            raise NotImplementedError("Undetected Chrome is not supported in this version")
            # return UndetectedChrome()
        if self.headless:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            return webdriver.Chrome(options=options)
        return webdriver.Chrome()

    def run_actions(self, actions: list[DriverAction], driver: webdriver.Chrome | None = None):
        _driver = driver if driver is not None else self.get_driver()
        results = []

        for action in actions:
            match action.action:
                case "url":
                    _driver.get(action.identifier)
                    self.log_msg(f"Opened URL: {action.identifier}", level='debug')
                case "send_keys":
                    _driver.find_element(By.CSS_SELECTOR, action.identifier).send_keys(action.input)
                    self.log_msg(f"Sent keys: {action.input} to {action.identifier}", level='debug')
                case "click":
                    _driver.find_element(By.CSS_SELECTOR, action.identifier).click()
                    self.log_msg(f"Clicked on: {action.identifier}", level='debug')
                case "sleep":
                    self.log_msg(f"Sleeping for: {action.input} seconds", level='debug')
                    sleep(action.input)
                case "get_text":
                    result = _driver.find_element(By.CSS_SELECTOR, action.identifier).text
                    results.append(result)
                    self.log_msg(f"Storing text: {result} at idx {len(results)-1}", level='debug')
                case "get_texts":
                    result = [element.text for element in _driver.find_elements(By.CSS_SELECTOR, action.identifier)]
                    results.append(result)
                    self.log_msg(f"Storing texts: {result} at idx {len(results)-1}", level='debug')
                case _:
                    self.log_msg(f"Invalid action: {action.action}", level='error')
                    if self.raise_exceptions:
                        raise ValueError(f"Invalid action: {action.action}")

        if driver is None:
            _driver.quit()

        return results
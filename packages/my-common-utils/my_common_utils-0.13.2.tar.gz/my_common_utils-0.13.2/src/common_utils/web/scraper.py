from dataclasses import dataclass
from typing import Literal
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

# from undetected_chromedriver.v2 import Chrome as UndetectedChrome


@dataclass
class DriverAction:
    action: Literal["url", "sleep", "click", "send_keys", "get_text", "get_texts"]
    identifier: str | None = None
    input: str | int | None = None



class SeleniumHandler:
    def __init__(self, headless: bool = True, undetected: bool = False):
        self.headless = headless
        self.undetected = undetected

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
                case "send_keys":
                    _driver.find_element(By.CSS_SELECTOR, action.identifier).send_keys(action.input)
                case "click":
                    _driver.find_element(By.CSS_SELECTOR, action.identifier).click()
                case "sleep":
                    sleep(action.input)
                case "get_text":
                    result = _driver.find_element(By.CSS_SELECTOR, action.identifier).text
                    results.append(result)
                case "get_texts":
                    result = [element.text for element in _driver.find_elements(By.CSS_SELECTOR, action.identifier)]
                    results.append(result)
                case _:
                    raise ValueError(f"Invalid action: {action.action}")

        if driver is None:
            _driver.quit()

        return results
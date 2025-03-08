from dataclasses import dataclass
from typing import Literal
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
import undetected_chromedriver as uc

from common_utils.logger import create_logger



@dataclass
class DriverAction:
    action: Literal["url", "sleep", "click", "send_keys", "get_text", "get_texts"]
    identifier: str | None = None
    input: str | int | None = None



class SeleniumHandler:
    log = create_logger("SeleniumHandler")

    def __init__(self,
                 headless: bool = False,
                 undetected: bool = False,
                 verbose: bool = True,
                 raise_exceptions: bool = True,
                 download_driver: bool = False
    ) -> None:
        self.headless = headless
        self.undetected = undetected
        self.verbose = verbose
        self.raise_exceptions = raise_exceptions
        self.download_driver = download_driver

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
        kwargs = {}
        if self.download_driver and not self.undetected:
            from selenium.webdriver.chrome.service import Service
            from webdriver_manager.chrome import ChromeDriverManager
            kwargs['service'] = Service(ChromeDriverManager().install())

        if self.headless and self.undetected:
            options = uc.ChromeOptions()
            options.add_argument("--headless")
            kwargs['options'] = options
        elif self.headless:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            kwargs['options'] = options

        if self.undetected:
            return uc.Chrome(**kwargs)
        else:
            return webdriver.Chrome(**kwargs)

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


if __name__ == '__main__':
    ud = SeleniumHandler(undetected=True).get_driver()
    ud.get("https://www.google.com")
    sleep(2)

    ud2 = SeleniumHandler(undetected=True, headless=True).get_driver()
    ud2.get("https://www.google.com")
    google_text = ud2.find_element(By.CSS_SELECTOR, 'body').text
    print(google_text)
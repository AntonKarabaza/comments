from abc import ABC, abstractmethod
from typing import List

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from comments.core.tools.property_reader import PropertyReader


class Driver(ABC):
    @abstractmethod
    def load(self, url: str):
        pass

    @abstractmethod
    def refresh(self):
        pass

    @abstractmethod
    def find_element(self, by: By, locator: str):
        pass

    @abstractmethod
    def find_elements(self, by: By, locator: str):
        pass

    @abstractmethod
    def stop(self):
        pass


class RemoteDriver(Driver):
    def __init__(self, driver: webdriver):
        self._driver = driver
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def load(self, url: str) -> webdriver:
        self._driver.get(url)
        return self

    def find_element(self, by: By, locator: str) -> WebElement:
        wait = WebDriverWait(self._driver, 5)
        element = wait.until(EC.presence_of_element_located((by, locator)))
        return element

    def find_elements(self, by: By, locator: str) -> List[WebElement]:
        wait = WebDriverWait(self._driver, 5)
        elements = wait.until(
            EC.presence_of_all_elements_located((by, locator)))
        return elements

    def refresh(self) -> webdriver:
        self._driver.refresh()
        return self

    def stop(self):
        if self._driver is not None:
            self._driver.delete_all_cookies()
            self._driver.close()
        self._driver = None


class WebDriverFactoryFromConfig:
    def init_driver(self):
        browser_name = PropertyReader('config.properties').get_browser_name()
        port = PropertyReader('config.properties').get_host()

        if browser_name.lower() == "chrome":
            try:
                capabilities = DesiredCapabilities.CHROME.copy()
                driver = webdriver.Remote(port, capabilities)
                return RemoteDriver(driver)
            except Exception:
                raise Exception("Can't initialize webdriver")
        elif browser_name.lower() == "firefox":
            try:
                capabilities = DesiredCapabilities.FIREFOX.copy()
                driver = webdriver.Remote(port, capabilities)
                return RemoteDriver(driver)
            except Exception:
                raise Exception("Can't initialize webdriver")
        else:
            raise Exception("Driver is not initialized.")

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class WebdriverUtils(object):
    def __init__(self, driver_name: str):
        self._driver_name = driver_name.lower()
        self._driver = None

    def get_driver(self):
        if self._driver is None:
            if self._driver_name == 'chrome':
                capabilities = DesiredCapabilities.CHROME.copy()
                port = 9515
            elif self._driver_name == 'firefox':
                capabilities = DesiredCapabilities.FIREFOX.copy()
                port = 4444
            else:
                raise Exception("Browser is not supported")
            try:
                self._driver = webdriver.Remote(port, capabilities)
            except Exception:
                raise Exception("Can't initialize webdriver")
            self._driver.implicitly_wait(10)
            self._driver.maximize_window()
        return self._driver

    def load(self, url: str):
        self.get_driver().get(url)

    def refresh(self):
        self.get_driver().refresh()

    def stop(self):
        if self._driver is not None:
            self._driver.delete_all_cookies()
            self._driver.close()
        self._driver = None


class WebDriverFactory:
    drivers = []

    def init_driver(self, driver_name: str, port: int):
        if driver_name.lower() == "chrome":
            try:
                capabilities = DesiredCapabilities.CHROME.copy()
                driver = webdriver.Remote(port, capabilities)
                self.drivers.append(driver)
                return driver
            except Exception:
                raise Exception("Can't initialize webdriver")
        elif driver_name.lower() == "firefox":
            try:
                capabilities = DesiredCapabilities.FIREFOX.copy()
                driver = webdriver.Remote(port, capabilities)
                self.drivers.append(driver)
                return driver
            except Exception:
                raise Exception("Can't initialize webdriver")

    def close_drivers(self):
        [driver.quit() for driver in self.drivers]

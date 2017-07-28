from selenium.webdriver.remote.webelement import WebElement


class Control(object):
    def __init__(self, element: WebElement):
        self._element = element

    def click(self):
        return self._element.click()

    def clear(self):
        return self._element.clear()

    def get_text(self):
        return self._element.text

    def get_attr(self, attribute):
        return self._element.get_attribute(attribute)

    def is_displayed(self):
        return self._element.is_displayed()

    def send_keys(self, text):
        return self._element.send_keys(text)

    def is_selected(self):
        return self._element.is_selected()

    def is_enabled(self):
        return self._element.is_enabled()

    def submit(self):
        return self._element.submit()

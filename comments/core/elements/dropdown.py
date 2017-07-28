from selenium.webdriver.support.select import Select

from abc import abstractmethod, ABC


class DropDown(ABC):
    @abstractmethod
    def select_by_text(self, text: str):
        pass

    @abstractmethod
    def select_by_value(self, value: str):
        pass

    @abstractmethod
    def select_by_index(self, index: int):
        pass

    @abstractmethod
    def is_enabled(self):
        pass


class RealDropDown(DropDown):
    def __init__(self, select: Select):
        self._select = select

    def select_by_text(self, text: str):
        self._select.select_by_visible_text(text)

    def select_by_value(self, value: str):
        self._select.select_by_value(value)

    def select_by_index(self, index: int):
        self._select.select_by_index(index)

    def is_enabled(self):
        return self._select.is_enabled()

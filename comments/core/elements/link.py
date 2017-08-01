from abc import abstractmethod, ABC

from comments.core.tools.control import Control


class ILink(ABC):
    @abstractmethod
    def click(self):
        pass

    @abstractmethod
    def get_text(self):
        pass

    @abstractmethod
    def get_href(self):
        pass

    @abstractmethod
    def is_displayed(self):
        pass

    @abstractmethod
    def is_enabled(self):
        pass


class Link(ILink):
    def __init__(self, control: Control):
        self._control = control

    def click(self):
        return self._control.click()

    def get_text(self):
        return self._control.get_text()

    def get_href(self):
        return self._control.get_attr('href')

    def is_displayed(self):
        return self._control.is_displayed()

    def is_enabled(self):
        return self._control.is_enabled()

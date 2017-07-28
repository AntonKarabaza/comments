from abc import abstractmethod, ABC

from comments.core.tools.control import Control


class Button(ABC):
    @abstractmethod
    def click(self):
        pass

    @abstractmethod
    def get_text(self):
        pass

    @abstractmethod
    def is_displayed(self):
        pass

    @abstractmethod
    def is_enabled(self):
        pass


class RealButton(Button):
    def __init__(self, control: Control):
        self._control = control

    def click(self):
        return self._control.click()

    def get_text(self):
        return self._control.get_text()

    def is_displayed(self):
        return self._control.is_displayed()

    def is_enabled(self):
        return self._control.is_enabled()

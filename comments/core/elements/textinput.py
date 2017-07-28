from abc import abstractmethod, ABC

from comments.core.tools.control import Control


class TextInput(ABC):
    @abstractmethod
    def click(self):
        pass

    @abstractmethod
    def submit(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def type(self, text):
        pass

    @abstractmethod
    def is_displayed(self):
        pass

    @abstractmethod
    def is_enabled(self):
        pass


class RealTextInput(TextInput):
    def __init__(self, control: Control):
        self._control = control

    def click(self):
        return self._control.click()

    def submit(self):
        return self._control.submit()

    def clear(self):
        return self._control.clear()

    def type(self, text):
        return self._control.send_keys(text)

    def is_displayed(self):
        return self._control.is_displayed()

    def is_enabled(self):
        return self._control.is_enabled()


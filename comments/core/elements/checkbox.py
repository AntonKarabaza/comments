from abc import abstractmethod, ABC

from comments.core.tools.control import Control


class CheckBox(ABC):
    @abstractmethod
    def check(self):
        pass

    @abstractmethod
    def uncheck(self):
        pass

    @abstractmethod
    def is_checked(self):
        pass

    @abstractmethod
    def is_enabled(self):
        pass


class RealCheckBox(CheckBox):
    def __init__(self, control: Control):
        self._control = control

    def check(self):
        if self._control.is_selected():
            self._control.click()

    def uncheck(self):
        if not self._control.is_selected():
            self._control.click()

    def is_checked(self):
        return self._control.is_selected()

    def is_enabled(self):
        return self._control.is_enabled()

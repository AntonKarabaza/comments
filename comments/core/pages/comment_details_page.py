from selenium.webdriver.common.by import By

from comments.core.elements.button import Button
from comments.core.elements.checkbox import CheckBox
from comments.core.elements.textinput import TextInput
from comments.core.pages import main_page
from comments.core.tools.control import Control
from comments.core.tools.webdriver_utils import Driver
from comments.core.tools.selectors import Comment


class CommentDetailsPage:
    def __init__(self, driver: Driver):
        self._driver = driver

    def click_save_button(self):
        Button(Control(self._driver.find_element(By.CSS_SELECTOR,
                                                 Comment.SAVE_BTN))).click()
        return self

    def click_save_and_return_button(self):
        Button(Control(self._driver.find_element(By.CSS_SELECTOR,
                                                 Comment.SAVE_RETURN_BTN))).click()
        return main_page.MainPage(self._driver)

    def input_comment_text(self, text: str):
        comment_text = TextInput(Control(self._driver.find_element(By.ID,
                                                                   Comment.EDIT_TEXT)))
        comment_text.clear()
        comment_text.type(text)
        return self

    def edit_comment_text(self, text: str):
        TextInput(Control(self._driver.find_element(By.ID, Comment.EDIT_TEXT))).type(text)
        return self

    def input_comment_number(self, text: str):
        comment_number = TextInput(Control(self._driver.find_element(By.ID,
                                                                     Comment.EDIT_NUMBER)))
        comment_number.clear()
        comment_number.type(text)
        return self

    def edit_comment_number(self, text: str):
        TextInput(Control(self._driver.find_element(By.ID, Comment.EDIT_NUMBER))).type(text)
        return self

    def check_active_status_checkbox(self):
        active_status = CheckBox(Control(self._driver.find_element(
            By.CSS_SELECTOR, Comment.ACTIVE)))
        if not active_status.is_checked():
            active_status.check()
        return self

    def uncheck_active_status_checkbox(self):
        active_status = CheckBox(Control(self._driver.find_element(By.CSS_SELECTOR, Comment.ACTIVE)))
        if active_status.is_checked():
            active_status.check()
        return self

    def click_select_all_categories(self):
        Button(Control(self._driver.find_element(By.NAME, Comment.SELECT_ALL_CAT_BTN))).click()
        return self

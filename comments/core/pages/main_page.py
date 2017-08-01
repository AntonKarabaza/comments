from comments.core.entities.category import Category
from comments.core.elements.button import RealButton
from comments.core.pages.comment_details_page import CommentDetailsPage
from comments.core.tools.control import Control

from selenium.webdriver.common.by import By

from comments.core.tools.webdriver_utils import Driver


class MainPage:
    def __init__(self, driver: Driver):
        self._driver = driver
        self._main_menu = MainMenu(self._driver)
        self._filter_menu = FilterMenu(self._driver)

    def click_new_button(self):
        return self._main_menu.click_new_button()

    def click_edit_button(self):
        return self._main_menu.click_edit_button()

    def click_delete_button(self):
        return self._main_menu.click_delete_button()

    def set_category_filter(self, category: Category):
        return self._filter_menu.set_filter_category(category)

    def set_status_filter(self, status: bool):
        return self._filter_menu.set_filter_status(status)

    def click_apply_filter(self):
        return self._filter_menu.apply_filter()


class MainMenu:
    def __init__(self, driver: Driver):
        self._driver = driver

    def click_new_button(self) -> CommentDetailsPage:
        RealButton(Control(self._driver.find_element(By.ID, "newbutton"))).click()
        return CommentDetailsPage(self._driver)

    def click_edit_button(self) -> CommentDetailsPage:
        RealButton(Control(self._driver.find_element(By.CSS_SELECTOR, "input[value='Edit..']"))).click()
        return CommentDetailsPage(self._driver)

    def click_delete_button(self) -> MainPage:
        RealButton(Control(self._driver.find_element(By.CSS_SELECTOR, "input[value='Delete']"))).click()
        return MainPage(self._driver)


class DialogMenu:
    def __init__(self, driver: Driver):
        self._driver = driver

    def confirm(self) -> MainPage:
        RealButton(Control(self._driver.find_element(By.CSS_SELECTOR, "div > button:nth-child(1)"))).click()
        return MainPage(self._driver)

    def cancel(self) -> MainPage:
        RealButton(Control(self._driver.find_element(By.CSS_SELECTOR, "div > button:nth-child(2)"))).click()
        return MainPage(self._driver)

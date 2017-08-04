from selenium.webdriver.support.select import Select

from comments.core.elements.checkbox import CheckBox
from comments.core.elements.link import Link
from comments.core.entities.category import Category
from comments.core.elements.button import Button
from comments.core.elements.dropdown import DropDown
from comments.core.entities.comment import Comment
from comments.core.pages.comment_details_page import CommentDetailsPage
from comments.core.tools.control import Control
from comments.core.tools.selectors import Comment as CommSelectors,\
    Paging, Dialog, MainMenu as Main, FilterMenu as Filter

from typing import List

from selenium.webdriver.common.by import By

from comments.core.tools.webdriver_utils import Driver


class MainPage:
    def __init__(self, driver: Driver):
        self._driver = driver
        self._main_menu = MainMenu(self._driver)
        self._filter_menu = FilterMenu(self._driver)
        self._comments_table = CommentsTable(self._driver)

    def click_new_button(self):
        return self._main_menu.click_new_button()

    def click_edit_button(self):
        return self._main_menu.click_edit_button()

    def click_delete_button(self):
        return self._main_menu.click_delete_button()

    def set_category_filter(self, category: Category):
        return self._filter_menu.set_category_filter(category)

    def set_status_filter(self, status: bool):
        return self._filter_menu.set_active_status_filter(status)

    def click_apply_filter(self):
        return self._filter_menu.apply_filter()

    def access_comments_table(self):
        return self._comments_table


class MainMenu:
    def __init__(self, driver: Driver):
        self._driver = driver

    def click_new_button(self) -> CommentDetailsPage:
        Button(Control(self._driver.find_element(By.ID, Main.NEW_BTN))).click()
        return CommentDetailsPage(self._driver)

    def click_edit_button(self) -> CommentDetailsPage:
        Button(Control(self._driver.find_element(
            By.CSS_SELECTOR, Main.EDIT_BTN))).click()
        return CommentDetailsPage(self._driver)

    def click_delete_button(self) -> MainPage:
        Button(Control(self._driver.find_element(
            By.CSS_SELECTOR, Main.DELETE_BTN))).click()
        return MainPage(self._driver)


class FilterMenu:
    def __init__(self, driver: Driver):
        self._driver = driver

    def set_category_filter(self, category: Category = None) -> MainPage:
        category_dropdown = DropDown(Select(self._driver.find_element(
            By.ID, Filter.CATEGORY_FILTER)))
        if category is None:
            category_dropdown.select_by_text("All")
        else:
            category_dropdown.select_by_text(category.get_category())
        return MainPage(self._driver)

    def set_active_status_filter(self, status: bool = None):
        status_dropdown = DropDown(Select(self._driver.find_element(
            By.ID, Filter.STATUS_FILTER)))
        if status is None:
            status_dropdown.select_by_text("All")
        elif status is True:
            status_dropdown.select_by_text("Active")
        else:
            status_dropdown.select_by_text("Inactive")
        return MainPage(self._driver)

    def apply_filter(self):
        Button(Control(self._driver.find_element(By.ID, Filter.APPLY_BTN))).click()
        return MainPage(self._driver)


class DialogMenu:
    def __init__(self, driver: Driver):
        self._driver = driver

    def confirm(self) -> MainPage:
        Button(Control(self._driver.find_element(
            By.CSS_SELECTOR, Dialog.YES_BTN))).click()
        return MainPage(self._driver)

    def cancel(self) -> MainPage:
        Button(Control(self._driver.find_element(
            By.CSS_SELECTOR, Dialog.NO_BTN))).click()
        return MainPage(self._driver)


class CommentsTable:
    def __init__(self, driver: Driver):
        self._driver = driver

    def get_all_comments(self) -> List[Comment]:
        comments = []

        while True:
            comments.extend(self.get_all_comments_from_page())
            if self._next_page_exists():
                self._go_next_page()
            else:
                return comments


    def get_all_comments_from_page(self) -> List[Comment]:
        comments = []

        comments.extend([self.get_comment_from_row(row_num) for row_num in
                        range(1, self.comments_count_on_page()+1)])
        return comments

    def get_comment_from_row(self, row: int) -> Comment:
        try:
            comment_id = int(self._driver.find_element(By.XPATH,
                CommSelectors.COMMENT_NUMBER_BY_ROW.format(row_num=row)).text)
        except ValueError:
            comment_id = None
        comment_text = self._driver.find_element(
            By.XPATH, CommSelectors.COMMENT_TEXT_BY_ROW.format(row_num=row)).text
        if self._driver.find_element(By.XPATH,
            CommSelectors.COMMENT_ACTIVE_BY_ROW.format(row_num=row)).text == "":
            comment_active = True
        else:
            comment_active = False
        categories = [Category(category) for category in
                      self._driver.find_element(By.XPATH,
                      CommSelectors.COMMENT_CATEGORY_BY_ROW.format(row_num=row))
                      .text.split("; ")]

        return Comment(comment_text, comment_active, comment_id, *categories)

    def _go_next_page(self):
        if self._next_page_exists():
            footer = self._driver.find_elements(By.CSS_SELECTOR,
                                                Paging.PAGING_LINKS)
            footer[-1].click()

    def _next_page_exists(self):
        footer = self._driver.find_elements(By.CSS_SELECTOR,
                                            Paging.PAGING_LINKS)

        paging_link = Link(Control(footer[-1]))
        if '>' in paging_link.get_text():
            return True
        else:
            return False

    def comments_count_on_page(self):
        return len(self._driver.find_elements(
            By.XPATH, CommSelectors.ROWS))

    def set_prev_page(self) -> MainPage:
        footer = self._driver.find_elements(By.CSS_SELECTOR,
                                            Paging.PAGING_LINKS)
        for element in footer:
            paging_link = Link(Control(element))
            if '<' in paging_link.get_text():
                paging_link.click()
        return MainPage(self._driver)

    def is_comment_present(self, comment: Comment) -> bool:
        if comment in self.get_all_comments():
            return True
        else:
            return False

    def is_all_comments_with_status(self, status: bool) -> bool:
        comments = self.get_all_comments()

        if status:
            for comment in comments:
                if not comment.is_active():
                    return False
        else:
            for comment in comments:
                if comment.is_active():
                    return False
        return True

    def select_comment_by_number(self, number: int) -> MainPage:
        CheckBox(Control(self._driver.find_element(
            By.XPATH, CommSelectors.COMMENT_CHECKBOX_BY_ROW\
            .format(row_num=number)))).check()

        return MainPage(self._driver)

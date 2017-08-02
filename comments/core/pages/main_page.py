from selenium.webdriver.support.select import Select

from comments.core.elements.link import Link
from comments.core.entities.category import Category
from comments.core.elements.button import Button
from comments.core.elements.dropdown import DropDown
from comments.core.entities.comment import Comment
from comments.core.pages.comment_details_page import CommentDetailsPage
from comments.core.tools.control import Control

from typing import List

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
        return self._filter_menu.set_category_filter(category)

    def set_status_filter(self, status: bool):
        return self._filter_menu.set_active_status_filter(status)

    def click_apply_filter(self):
        return self._filter_menu.apply_filter()


class MainMenu:
    def __init__(self, driver: Driver):
        self._driver = driver

    def click_new_button(self) -> CommentDetailsPage:
        Button(Control(self._driver.find_element(By.ID, "newbutton"))).click()
        return CommentDetailsPage(self._driver)

    def click_edit_button(self) -> CommentDetailsPage:
        Button(Control(self._driver.find_element(
            By.CSS_SELECTOR, "input[value='Edit..']"))).click()
        return CommentDetailsPage(self._driver)

    def click_delete_button(self) -> MainPage:
        Button(Control(self._driver.find_element(
            By.CSS_SELECTOR, "input[value='Delete']"))).click()
        return MainPage(self._driver)


class FilterMenu:
    def __init__(self, driver: Driver):
        self._driver = driver

    def set_category_filter(self, category: Category = None) -> MainPage:
        category_dropdown = DropDown(Select(self._driver.find_element(
            By.ID, "SelectedCateg")))
        if category is None:
            category_dropdown.select_by_text("All")
        else:
            category_dropdown.select_by_text(category.get_category())
        return MainPage(self._driver)

    def set_active_status_filter(self, status: bool = None):
        status_dropdown = DropDown(Select(self._driver.find_element(
            By.ID, "SelectedStatus")))
        if status is None:
            status_dropdown.select_by_text("All")
        elif status is True:
            status_dropdown.select_by_text("Active")
        else:
            status_dropdown.select_by_text("Inactive")
        return MainPage(self._driver)

    def apply_filter(self):
        Button(Control(self._driver.find_element(By.ID, "applybutton"))).click()
        return MainPage(self._driver)


class DialogMenu:
    def __init__(self, driver: Driver):
        self._driver = driver

    def confirm(self) -> MainPage:
        Button(Control(self._driver.find_element(
            By.CSS_SELECTOR, "div > button:nth-child(1)"))).click()
        return MainPage(self._driver)

    def cancel(self) -> MainPage:
        Button(Control(self._driver.find_element(
            By.CSS_SELECTOR, "div > button:nth-child(2)"))).click()
        return MainPage(self._driver)


class CommentsTable:
    def __init__(self, driver: Driver):
        self._driver = driver

    def get_all_comments(self) -> List[Comment]:
        comments = []
        for element in self._driver.find_elements(By.CSS_SELECTOR,
                                                  ".webgrid-footer > td > a"):
            comments.append([self.get_comment_from_row(row_num) for row_num in
                             range(1, self.comments_count_on_page())])
            paging_link = Link(Control(element))
            if '>' in paging_link.get_text():
                paging_link.click()
        return comments

    def get_comment_from_row(self, row: int) -> Comment:
        table_row = self._driver.find_element(
            By.XPATH, "//form[@name='commentsSelect']/table/tbody/tr[{row_num}]"
                .format(row_num=row))

        comment_id = int(table_row.find_element(
            By.XPATH, "/td[@class='numbercolumn']").text)
        comment_text = table_row.find_element(
            By.XPATH, "/td[@class='textcolumn']").text
        if table_row.find_element(
                By.XPATH, "/td[@class='inactivecolumn']").text == "":
            comment_active = True
        else:
            comment_active = False
        categories = [Category(categorie.strip("Cat")) for categorie in
                      table_row.find_element(By.XPATH,
                                             "/td[@class='categorycolumn']").text.split(
                          "; ")]

        return Comment(comment_id, comment_text, comment_active, *categories)

    def set_next_page(self) -> MainPage:
        footer = self._driver.find_elements(By.CSS_SELECTOR,
                                            ".webgrid-footer > td > a")
        for element in footer:
            paging_link = Link(Control(element))
            if '>' in paging_link.get_text():
                paging_link.click()
        return MainPage(self._driver)

    def comments_count_on_page(self):
        return len(self._driver.find_elements(
            By.XPATH, "//form[@name='commentsSelect']/table/tbody/tr"))

    def set_prev_page(self) -> MainPage:
        footer = self._driver.find_elements(By.CSS_SELECTOR,
                                            ".webgrid-footer > td > a")
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
        pass

    def is_all_comments_contain_category(self, category: Category) -> bool:
        pass

    def select_comment_by_number(self, number: int) -> MainPage:
        rows = self._driver.find_elements(
            By.XPATH, "//form[@name='commentsSelect']/table/tbody/tr")
        for element in rows:
            if int(element.find_element(
                    By.XPATH, "/td[@class='numbercolumn']").text) == number:
                element.find_element(
                    By.CSS_SELECTOR, 'td.checkedcolumn > input['
                                     'type="checkbox"]').click()
        return MainPage(self._driver)

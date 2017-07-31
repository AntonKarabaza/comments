from comments.core.entities.category import Category


class MainPage:
    def __init__(self):
        self._main_menu = MainMenu()
        self._filter_menu = FilterMenu()

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


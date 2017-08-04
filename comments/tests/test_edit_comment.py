from comments.core.entities.category import Category
from comments.core.entities.comment import Comment
from comments.core.pages.main_page import MainPage


def test_edit(webdriver_on_main_page):
    assert MainPage(webdriver_on_main_page)\
            .access_comments_table()\
            .select_comment_by_number(1)\
            .click_edit_button()\
            .edit_comment_text(" Edited")\
            .click_save_and_return_button()\
            .access_comments_table()\
            .get_comment_from_row(1) == \
            Comment("Comment Text 0 Edited", True, 0, Category("Cat0"))

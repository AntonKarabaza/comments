from comments.core.entities.category import Category
from comments.core.entities.comment import Comment
from comments.core.pages.main_page import MainPage


def test_create(webdriver_setup):
    comments_list = MainPage(webdriver_setup
        .load('http://commentssprintone.azurewebsites.net')) \
        .click_new_button() \
        .input_comment_text('new') \
        .input_comment_number('123') \
        .click_select_all_categories() \
        .click_save_and_return_button().access_comments_table().get_all_comments()
    comment = Comment(123, 'new', True,
                      *[Category('Cat0'), Category('Cat1'), Category('Cat2'),
                        Category('Cat3'), Category('Cat4'), Category('Cat5')])

    assert comment in comments_list

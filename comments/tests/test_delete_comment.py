from comments.core.pages.main_page import MainPage


def test_delete_comment(webdriver_on_main_page):
    main_page = MainPage(webdriver_on_main_page)
    comment = main_page.access_comments_table().get_comment_from_row(1)
    comments_list = main_page.access_comments_table().select_comment_by_number(
        1).click_delete_button().confirm().access_comments_table().get_all_comments()

    assert comment not in comments_list

from comments.core.pages.main_page import MainPage


def test_comment_active_status(webdriver_on_main_page):
    assert MainPage(webdriver_on_main_page)\
            .set_status_filter(True)\
            .click_apply_filter()\
            .access_comments_table()\
            .is_all_comments_with_status(True)

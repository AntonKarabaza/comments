class Comment:
    ROWS = "//form[@name='commentsSelect']/table/tbody/tr"
    COMMENT_NUMBER_BY_ROW = "//form[@name='commentsSelect']/table/tbody/" \
                            "tr[{row_num}]/td[@class='numbercolumn']"
    COMMENT_TEXT_BY_ROW = "//form[@name='commentsSelect']/table/tbody/" \
                          "tr[{row_num}]/td[@class='textcolumn']"
    COMMENT_ACTIVE_BY_ROW = "//form[@name='commentsSelect']/table/tbody/" \
                            "tr[{row_num}]/td[@class='inactivecolumn']"
    COMMENT_CATEGORY_BY_ROW = "//form[@name='commentsSelect']/table/tbody/" \
                              "tr[{row_num}]/td[@class='categorycolumn']"
    CHECKBOX = 'td.checkedcolumn > input[type="checkbox"]'
    EDIT_NUMBER = "Number"
    EDIT_TEXT = "Text"
    SAVE_BTN = "#editor-navigation > input:nth-child(2)"
    SAVE_RETURN_BTN = "#editor-navigation > input:nth-child(3)"
    ACTIVE = "#Active"
    SELECT_ALL_CAT_BTN = "AllSelect"


class Paging:
    PAGING_LINKS = ".webgrid-footer > td > a"


class Dialog:
    YES_BTN = "div > button:nth-child(1)"
    NO_BTN = "div > button:nth-child(2)"


class MainMenu:
    NEW_BTN = "newbutton"
    EDIT_BTN = "input[value='Edit..']"
    DELETE_BTN = "input[value='Delete']"


class FilterMenu:
    CATEGORY_FILTER = "SelectedCateg"
    STATUS_FILTER = "SelectedStatus"
    APPLY_BTN = "applybutton"

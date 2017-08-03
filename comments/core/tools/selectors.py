class Comment:
    COMMENT_NUMBER_BY_ROW = "//form[@name='commentsSelect']/table/tbody/" \
                            "tr[{row_num}]/td[@class='numbercolumn']"
    COMMENT_TEXT_BY_ROW = "//form[@name='commentsSelect']/table/tbody/" \
                            "tr[{row_num}]/td[@class='textcolumn']"
    COMMENT_ACTIVE_BY_ROW = "//form[@name='commentsSelect']/table/tbody/" \
                            "tr[{row_num}]/td[@class='inactivecolumn']"
    COMMENT_CATEGORY_BY_ROW = "//form[@name='commentsSelect']/table/tbody/" \
                            "tr[{row_num}]/td[@class='categorycolumn']"
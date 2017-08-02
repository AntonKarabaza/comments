from comments.core.entities.category import Category
from typing import List


class Comment:
    def __init__(self, comm_id: int, comm_text: str, is_active: bool,
                 *comm_category: Category):
        self._id = comm_id
        self._text = comm_text
        self._is_active = is_active
        self._category = comm_category

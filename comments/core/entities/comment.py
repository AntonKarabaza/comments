from comments.core.entities.category import Category
from typing import List


class Comment:
    def __init__(self, comm_id, comm_text, is_active, *comm_category: Category):
        self._id = comm_id
        self._text = comm_text
        self._is_active = is_active
        self._category = comm_category

    def get_text(self) -> str:
        return str(self._text)

    def get_id(self) -> int:
        return int(self._id)

    def is_active(self) -> bool:
        if self._is_active.lower() == 'true':
            return True
        else:
            return False

    def get_categories(self) -> List[Category]:
        return list(self._category)

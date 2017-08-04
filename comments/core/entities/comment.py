from comments.core.entities.category import Category


class Comment:
    def __init__(self, comm_text: str, is_active: bool, comm_id: int = None,
                 *comm_category: Category):
        self._id = comm_id
        self._text = comm_text
        self._is_active = is_active
        self._category = comm_category

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

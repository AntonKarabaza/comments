class Category:
    def __init__(self, category: int):
        if category > 5 or category < 0:
            raise Exception('Category can\'t be created')
        else:
            self._category = category

    def get_category(self) -> str:
        return 'Cat' + str(self._category)

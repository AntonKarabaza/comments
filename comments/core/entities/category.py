class Category:
    def __init__(self, category):
            self._category = category

    def get_category(self) -> str:
        try:
            category_number = int(self._category)
            return 'Cat' + str(category_number)
        except ValueError:
            return self._category

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
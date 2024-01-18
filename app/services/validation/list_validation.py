from .validation import Validation


class ListValidation(Validation):

    def __init__(self):
        super().__init__(list)

    def is_valid(self, item):
        return self.is_of_type(item)

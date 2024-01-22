from .validation import Validation


class DictValidation(Validation):

    def __init__(self, structure):
        super().__init__(dict)

    def is_valid(self, item):
        return self.is_of_type(item)

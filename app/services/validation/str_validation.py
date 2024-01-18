from services.validation.exceptions import ValidationException
from .validation import Validation


class StringValidation(Validation):

    def __init__(self, blank = False):
        self.blank = blank
        super().__init__(str)

    def is_valid(self, item: str) -> bool:
        if not self.blank and not item:
            raise ValidationException('{} should not be blank')
        return self.is_of_type(item)

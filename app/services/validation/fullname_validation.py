from services.validation.exceptions import ValidationException
from .str_validation import StringValidation


class FullNameValidation(StringValidation):

    def __init__(self):
        super().__init__()

    def is_valid(self, item):
        super().is_valid(item)
        if len(item.split()) < 3:
            raise ValidationException('{} should contain first name, last name and patronym')

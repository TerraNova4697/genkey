from services.validation.exceptions import ValidationException
from .validation import Validation


class IntegerValidation(Validation):

    def __init__(self, min, max):
        self.min = min
        self.max = max
        super().__init__(int)

    def is_valid(self, item) -> bool:
        if item < self.min:
            raise ValidationException('{} should not be less then ' + str(self.min))
        if item > self.max:
            raise ValidationException('{} should not be greater then ' + str(self.max))

        return self.is_of_type(item)

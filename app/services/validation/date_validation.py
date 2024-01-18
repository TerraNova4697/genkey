from datetime import date

from services.validation.exceptions import ValidationException

from .validation import Validation


class DateValidation(Validation):

    def __init__(self, future: bool = True):
        self.future = future
        super().__init__(date)

    def is_valid(self, item):
        item = date.fromtimestamp(item)
        self.is_of_type(item)
        if self.future:
            today = date.today()
            if item <= today:
                raise ValidationException('{} should be later then ' + today.strftime('%d/%m/%y'))
        return True

    def is_future(self, item):
        if self.future:
            item > date.today()

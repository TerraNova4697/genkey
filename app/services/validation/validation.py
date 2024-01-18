from .exceptions import ValidationException


class Validation:

    def __init__(self, of_type):
        self.of_type = of_type

    def is_of_type(self, item) -> bool:
        if not item.__class__.__name__ != self.of_type.__class__.__name__:
            raise ValidationException('{} is not of type ' + self.of_type.__class__.__name__)

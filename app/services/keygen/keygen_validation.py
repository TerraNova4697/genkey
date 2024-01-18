from werkzeug.exceptions import BadRequest
from services.validation.fullname_validation import FullNameValidation

from services.validation.exceptions import ValidationException
from services.validation import (
    IntegerValidation, DateValidation, ListValidation
)


class KeygenValidation:
    MANDATORY_KEYS = {
        'devices_amount': IntegerValidation(min=10, max=50000),
        'expiration_date': DateValidation(),
        'services': ListValidation(),
        'fullname': FullNameValidation()
    }

    def __init__(self):
        pass

    def is_valid(self, data) -> bool:
        for param, validator in self.MANDATORY_KEYS.items():
            try:
                validator.is_valid(data[param])
            except ValidationException as exception:
                raise BadRequest(str(exception).format(param))
            except KeyError as exception:
                raise BadRequest(f'{param} parameter is mandatory')

        return True

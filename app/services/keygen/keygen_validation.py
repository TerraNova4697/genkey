from werkzeug.exceptions import BadRequest
from services.validation.fullname_validation import FullNameValidation

from services.validation.exceptions import ValidationException
# from services.validation import (
#     IntegerValidation, DateValidation, ListValidation
# )
from jsonschema import validate


class KeygenValidation:
    # MANDATORY_KEYS = {
        # 'company': StringValidation(),
        # 'person': DictValidation(),
        # 'payment': DictValidation(),
        # 'expires_at': DateValidation(),
        # 'services': ListValidation(),
        # 'issued_at': StringValidation(),
        # 'device_id': StringValidation()
        # 'devices_amount': IntegerValidation(min=10, max=50000),
        # 'expiration_date': DateValidation(),
        # 'services': ListValidation(),
        # 'fullname': FullNameValidation()
    # }

    keygen_request_schema = {
        "type": "object",
        "properties": {
            "company": {"type": "string"},
            "person": {
                "type": "object",
                "properties": {
                    "fname": {"type": "string"},
                    "lname": {"type": "string"},
                    "fname": {"type": "string"},
                },
                "required": ["fname", "lname"]
            },
            "payment": {
                "type": "object",
                "properties": {
                    "status": {"type": "string"},
                    "amount": {"type": "integer"},
                    "created_at": {"type": "integer"}
                },
                "required": ["status", "amount", "created_at"]
            },
            "expires_at": {"type": "integer"},
            "services": {
                "type": "array",
                "minItems": 1,
                "items": {"type": "integer"}
            },
            "issued_for": {"type": "string"},
            "device_id": {"type": "string"}
        },
        "required": ["company", "person", "payment", "expires_at", "services", "issued_for", "device_id"]
    }

    def __init__(self):
        pass

    def is_valid(self, data) -> bool:
        try:
            validate(data, schema=self.keygen_request_schema)
        except Exception as ex:
            print(ex)
            raise ValidationException(str(ex))

        return True

from services.validation.exceptions import ValidationException
from jsonschema import validate


class KeygenValidation:

    keygen_request_schema = {
        "type": "object",
        "properties": {
            "company": {"type": "string"},
            "companyPhone": {"type": "string"},
            "companyEmail": {"type": "string"},
            "person": {
                "type": "object",
                "properties": {
                    "fname": {"type": "string"},
                    "lname": {"type": "string"},
                    "email": {"type": "string"},
                    "phone": {"type": "string"},
                },
                "required": ["fname", "lname", "email"],
            },
            "payment": {
                "type": "object",
                "properties": {
                    "status": {"type": "integer"},
                    "amount": {"type": "integer"},
                    "created_at": {"type": "integer"},
                },
                "required": ["status", "amount", "created_at"],
            },
            "expires_at": {"type": "integer"},
            "services": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "type": "integer",
                },
            },
            "devices": {"type": "integer"},
            "issued_for": {"type": "string"},
            "device_id": {"type": "string"},
        },
        "required": [
            "company",
            "companyEmail",
            "person",
            "payment",
            "expires_at",
            "services",
            "issued_for",
            "device_id",
            "devices",
        ],
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

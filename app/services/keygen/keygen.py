import os
from datetime import date
from services.validation.exceptions import ItemNotFound
from models import Device

from services.keygen.keygen_validation import KeygenValidation
import jwt
from sqlalchemy.exc import NoResultFound

from database import db


class KeyGenerator:

    def __init__(self, data):
        self.data = data
        self._keygen_validation = KeygenValidation()

    def is_valid(self) -> bool:
        return self._keygen_validation.is_valid(data=self.data)

    def calculate_device_num(self, services) -> int:
        total = 0
        for service in services:
            total += service[1]
        return total

    def generate_key(self):
        try:
            device = db.session.execute(
                db.select(Device).filter_by(device_id=self.data["device_id"])
            ).scalar_one()
        except NoResultFound:
            raise ItemNotFound("Устройство с таким ID в системе не найдено")

        payload = {
            "created_at": int(date.today().strftime("%s")),
            "devices": self.data["devices"],
            "services": self.data["services"],
            "expires_at": self.data["expires_at"],
            "issued_for": self.data["issued_for"],
            "device_id": self.data["device_id"],
        }
        return jwt.encode(payload, device.secret_key, algorithm="HS256")

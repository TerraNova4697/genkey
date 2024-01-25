from http.client import HTTPException
import uuid
import secrets

from services.validation.exceptions import ItemNotFound, ValidationException
from flask import Blueprint, request

from services.keygen import KeyGenerator
from services import handle_keygen_data
from models import Device
from database import db


api_bp = Blueprint(
    'api_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/assets'
)


@api_bp.route('/', methods=['POST'])
def genkey():

    if request.method == 'POST':
        req_data = request.get_json()
        keygen = KeyGenerator(req_data)
        try:
            if keygen.is_valid():
                key = keygen.generate_key()
                payload = handle_keygen_data(req_data, key)
                payload['status'] = 200

                return payload
        except ValidationException as exception:
            message = str(exception).replace('\n', ' ')
            return {"status": 400, "message": str(message)}
        except ItemNotFound as exception:
            return {
                'status': 404,
                'message': str(exception)
            }


@api_bp.route('/generate-id', methods=['GET'])
def gen_id():
    time_based_uuid = uuid.uuid1()
    secret_key = secrets.token_urlsafe(32)
    device = Device(device_id=time_based_uuid, secret_key=secret_key)
    db.session.add(device)
    db.session.commit()

    return {
        'status': 200,
        'device_id': time_based_uuid,
        'secret_key': secret_key
    }

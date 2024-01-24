from services.validation.exceptions import ValidationException
from flask import Blueprint, request

from services.keygen import KeyGenerator
from services import handle_keygen_data


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

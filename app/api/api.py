from flask import Blueprint, request

from services.keygen import KeyGenerator
# from app.app import db
# from models import Company


api_bp = Blueprint(
    'api_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/assets'
)




@api_bp.route('/', methods=['GET', 'POST'])
def index():
    from app.app import db
    # if request.method == 'GET':
    #     data = request.get_json()
    #     key = jwt.decode(data.key, 'sectet', algorithms='HS256')
    #     return json.dumps({
    #         "decoded": key
    #     })
    if request.method == 'POST':
        keygen = KeyGenerator(request.get_json())
        if keygen.is_valid():
            key = keygen.generate_key()
            return {
                'status': 200,
                'key': key
            }


# @api_bp.route('/key', methods=['POST'])
# def key():
#     data = request.get_json()
#     print(data)
#     key = jwt.decode(data['key'], 'jkOA2ZgSNGig8nbYia1KUw', algorithms='HS256')
#     return json.dumps({
#         "decoded": key
#     })

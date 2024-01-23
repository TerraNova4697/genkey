from flask import Blueprint, jsonify, request

from services.keygen import KeyGenerator
from database import db
from models import Company, Payment, Person, Key, key_schema, company_schema, person_schema
from services import handle_keygen_data


api_bp = Blueprint(
    'api_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/assets'
)


@api_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        req_data = request.get_json()
        keygen = KeyGenerator(req_data)
        if keygen.is_valid():
            key = keygen.generate_key()
            handle_keygen_data(req_data, key)
            key_model = Key.query.join(Company).filter_by(key=key).first()

            # company = Company.query.last()
            # companies = Company.query.where(Company.fullname==req_data['company']).all()
            return {
                'status': 200,
                'key': key_schema.dump(key_model)
                # 'company': company_schema.dump(com),
                # 'companies': companies_schema.dump(companies),
                # 'person': person_schema.dump(person)
            }
    # if request.method == 'GET':
    #     payment = Payment(payment_amount=100.0, status='Completed')
    #     db.session.add(payment)
    #     db.session.commit()
    #     payment_schema = PaymentSchema()
    #     payment_json = payment_schema.dump(payment)
    #     print(payment_json)
    #     payments = Payment.query.all()
    #     return {
    #         'payments': payment_schema.dump(payments)
    #     }

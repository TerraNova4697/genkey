import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from database import db
from api.api import api_bp
from general.general import general_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(general_bp)
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    return app


# def setup_database(app):
#     with app.app_context():
#         db.create_all()
#     user = User()
#     user.username = "Tom"
#     db.session.add(user)
#     db.session.commit()


# app = Flask(__name__)

# from api.api import api_bp
# from general.general import general_bp
# from models import *

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)



if __name__ == '__main__':
    app = create_app()
    migrate = Migrate(app, db)
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')

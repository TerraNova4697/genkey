import os
from flask_migrate import Migrate
from flask import Flask

# from database import db, ma
from database import init_db, create_migrate
from api.api import api_bp
from general.general import general_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    init_db(app)
    app.register_blueprint(general_bp)
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    return app


app = create_app()
migrate = create_migrate(app)
app.run(debug=True, host='0.0.0.0')

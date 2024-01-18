import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from api.api import api_bp
from general.general import general_bp
from models import *

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(general_bp)
app.register_blueprint(api_bp, url_prefix='/api/v1')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()


def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
    ma.init_app(app)


def create_migrate(app):
    return Migrate(app, db)

from app import db
from sqlalchemy.dialects.postgresql import JSON


class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(128))

    def __init__(self, fullname):
        self.fullname = fullname

    def __repr__(self):
        return '<id {}>'.format(self.id)

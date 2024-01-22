from dataclasses import dataclass
from datetime import date

from database import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from marshmallow import Schema, fields, EXCLUDE
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass


class Base(DeclarativeBase, MappedAsDataclass):
    pass


# class Base(DeclarativeBase):
#     metadata = MetaData(naming_convention={
#         "ix": 'ix_%(column_0_label)s',
#         "uq": "uq_%(table_name)s_%(column_0_name)s",
#         "ck": "ck_%(table_name)s_%(constraint_name)s",
#         "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
#         "pk": "pk_%(table_name)s"
#     })


class Company(db.Model):
    __tablename__ = 'companies'

    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(db.String(128))

    def __repr__(self):
        return 'id: {}, fullname: {}'.format(self.id, self.fullname)


# class CompanySchema(Schema):
#     id = fields.Int()
#     fullname = fields.Str()


class Payment(db.Model):
    __tablename__ = 'payments'

    id: Mapped[int] = db.Column(db.Integer, primary_key=True)
    created_at: Mapped[str] = db.Column(db.Date, server_default=func.now())
    updated_at: Mapped[str] = db.Column(db.Date, onupdate=func.now())
    payment_amount: Mapped[int] = db.Column(db.Float, nullable=False)
    status: Mapped[str] = db.Column(db.Enum('Pending', 'Completed', 'Failed', name='payment_status'), nullable=False)
    keys: Mapped[int] = relationship('Key', backref='payment', lazy=True)

    def __repr__(self):
        return 'id: {}, status: {}'.format(self.id, self.status)


class Person(db.Model):
    __tablename__ = 'persons'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, server_default=func.now())
    updated_at = db.Column(db.Date, onupdate=func.now())
    fname = db.Column(db.String(64))
    lname = db.Column(db.String(64))
    patronym = db.Column(db.String(64), nullable=True)
    company = relationship('Company')


# class PaymentSchema(Schema):
#     id = fields.Int()
#     created_at = fields.DateTime(format='%Y-%m-%d%z')
#     updated_at = fields.DateTime(format='%Y-%m-%d%z')
#     payment_amount = fields.Float()
#     status = fields.Str()


class Key(db.Model):
    __tablename__ = 'keys'

    key = db.Column(db.String, primary_key=True)
    created_at = db.Column(db.Date, server_default=func.now())
    updated_at = db.Column(db.Date, onupdate=func.now())
    issuer = db.Column(db.String(128))
    payment_id = db.Column(db.Integer, db.ForeignKey('payments.id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)

    def __repr__(self):
        return f'Key. Issuer: {self.issuer}'


class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))

    def __repr__(self):
        return f'{self.name}'


class PaymentSchema(Schema):
    class Meta:
        model = Payment
        include_fk = True
        unknown = EXCLUDE


class CompanySchema(Schema):
    class Meta:
        model = Company
        unknown = EXCLUDE


class KeySchema(Schema):
    class Meta:
        model = Key
        include_fk = True
        unknown = EXCLUDE


# @dataclass
# class Key(db.Model):
#     __tablename__ = 'keys'
#     id: int
#     created_at: date
#     issuer: str

from dataclasses import dataclass
from datetime import date

from database import db, ma
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from marshmallow import Schema, fields, EXCLUDE
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass


# class Base(DeclarativeBase, MappedAsDataclass):
#     pass


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

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(128))
    persons = relationship('Person', back_populates='company')
    keys = relationship('Key', back_populates='company')

    def __repr__(self):
        return 'id: {}, fullname: {}'.format(self.id, self.fullname)


class Person(db.Model):
    __tablename__ = 'persons'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, server_default=func.now())
    updated_at = db.Column(db.Date, onupdate=func.now())
    fname = db.Column(db.String(64))
    lname = db.Column(db.String(64))
    patronym = db.Column(db.String(64), nullable=True)
    company_id = mapped_column(db.ForeignKey('companies.id'))
    company = relationship('Company', back_populates='persons')


class Key(db.Model):
    __tablename__ = 'keys'

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(1024))
    created_at = db.Column(db.Date, server_default=func.now())
    updated_at = db.Column(db.Date, onupdate=func.now())
    issuer = db.Column(db.String(128))
    payments = relationship('Payment', back_populates='key')
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    company = relationship('Company', back_populates='keys')

    def __repr__(self):
        return f'Key. Issuer: {self.issuer}'


class Payment(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date, onupdate=func.now())
    payment_amount = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Enum('Pending', 'Completed', 'Failed', name='payment_status'), nullable=False)
    key_id = db.Column(db.Integer, db.ForeignKey('keys.id'))
    key = relationship('Key', back_populates='payments')

    def __repr__(self):
        return 'id: {}, status: {}'.format(self.id, self.status)



# class PaymentSchema(Schema):
#     id = fields.Int()
#     created_at = fields.DateTime(format='%Y-%m-%d%z')
#     updated_at = fields.DateTime(format='%Y-%m-%d%z')
#     payment_amount = fields.Float()
#     status = fields.Str()





# class Service(db.Model):
#     __tablename__ = 'services'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(256))

#     def __repr__(self):
#         return f'{self.name}'


# class PaymentSchema(Schema):
#     class Meta:
#         model = Payment
#         include_fk = True
#         unknown = EXCLUDE


class CompanySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Company
        include_fk = True
        # unknown = EXCLUDE
        # fields = ('id', 'fullname')


class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        # include_fk = True
        # unknown = EXCLUDE
        fields = ('fname', 'lname', 'patronym')
    # id = ma.auto_field()
    fname = ma.auto_field()
    lname = ma.auto_field()
    patronym = ma.auto_field()
    # company = ma.auto_field()


class KeySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Key
        fields = ('key', )

    # id = ma.auto_field()
    key = ma.auto_field()
    # created_at = ma.auto_field()
    # updated_at = ma.auto_field()
    # issuer = ma.auto_field()
    # payments = ma.auto_field()
    # company = ma.auto_field()


class PaymentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Payment

    id = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()
    payment_amount = ma.auto_field()
    status = ma.auto_field()
    key = ma.auto_field()


company_schema = CompanySchema()
companies_schema = CompanySchema(many=True)
person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)
key_schema = KeySchema()
keys_schema = KeySchema(many=True)
payment_schema = PaymentSchema()
payments_schema = PaymentSchema(many=True)


# class KeySchema(Schema):
#     class Meta:
#         model = Key
#         include_fk = True
#         unknown = EXCLUDE


# @dataclass
# class Key(db.Model):
#     __tablename__ = 'keys'
#     id: int
#     created_at: date
#     issuer: str

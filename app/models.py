from database import db, ma
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, mapped_column


class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(128))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(128))
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
    email = db.Column(db.String(128))
    phone = db.Column(db.String(128))
    company_id = mapped_column(db.ForeignKey('companies.id'))
    company = relationship('Company', back_populates='persons')


class Device(db.Model):
    __tablename__ = 'devices'

    device_id = db.Column(db.String(256), primary_key=True)
    secret_key = db.Column(db.String(128))

    def __repr__(self):
        return f'{self.device_id}'


class Key(db.Model):
    __tablename__ = 'keys'

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(1024))
    created_at = db.Column(db.Date, server_default=func.now())
    updated_at = db.Column(db.Date, onupdate=func.now())
    issuer = db.Column(db.String(128))
    device_id = db.Column(db.String(256))
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


class CompanySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Company
        include_fk = True


class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        fields = ('fname', 'lname', 'phone', 'email')

    fname = ma.auto_field()
    lname = ma.auto_field()
    phone = ma.auto_field()
    email = ma.auto_field()


class KeySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Key
        fields = ('key', )

    key = ma.auto_field()


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

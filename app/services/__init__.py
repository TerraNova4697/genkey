from datetime import date

from models import (
    Company, Person, Key, Payment, companies_schema, company_schema, person_schema, persons_schema
)
from database import db


def handle_keygen_data(data, key):
    company = Company(fullname=data['company'])
    db.session.add(company)
    db.session.commit()

    person = Person(
        fname=data['person']['fname'],
        lname=data['person']['lname'],
        patronym=data['person'].get('patronym'),
        company=company
    )
    db.session.add(person)
    db.session.commit()

    key = Key(
        key=key,
        company=company,
        issuer=company.fullname,
    )
    db.session.add(key)
    db.session.commit()

    dt = date.fromtimestamp(data['payment']['created_at'])
    payment = Payment(
        payment_amount=data['payment']['amount'],
        status=data['payment']['status'],
        created_at=dt,
        key=key
    )
    db.session.add(payment)
    db.session.commit()

from datetime import datetime, timedelta
from typing import List

from sqlalchemy import or_, extract
from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas import ContactModel


async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()


async def get_contact(contact_id: int, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def create_contact(body: ContactModel, db: Session) -> Contact:
    contact = Contact(
        name=body.name,
        email=body.email,
        phone_number=body.phone_number,
        birth_date=body.birth_date,
        additional_data=body.additional_data
    )
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(contact_id: int, body: ContactModel, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.name = body.name
        contact.email = body.email
        contact.phone_number = body.phone_number
        contact.birth_date = body.birth_date
        contact.additional_data = body.additional_data
        db.commit()
    return contact


async def remove_contact(contact_id: int, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def search_contacts(query: str, db: Session):
    contacts = (
        db.query(Contact)
        .filter(
            or_(
                Contact.name.contains(query),
                Contact.email.contains(query)
            )
        )
        .all()
    )
    return contacts


async def get_birthdays(db: Session):
    today = datetime.today()
    end_date = today + timedelta(days=7)
    contacts = (
        db.query(Contact)
        .filter(
            ((extract('month', Contact.birth_date) == today.month) & (
                    extract('day', Contact.birth_date) >= today.day)) |
            ((extract('month', Contact.birth_date) == end_date.month) & (
                    extract('day', Contact.birth_date) <= end_date.day))
        )
        .all()
    )
    return contacts

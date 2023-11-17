from pydantic import BaseModel
from datetime import date

class ContactModel(BaseModel):
    name: str
    email: str
    phone_number: str
    birth_date: date
    additional_data: str

class ResponseContact(BaseModel):
    id: int
    name: str
    email: str
    phone_number: str
    birth_date: date
    additional_data: str

    class Config:
        from_attrs = True
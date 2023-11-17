from sqlalchemy import Column, Integer, String ,ARRAY
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    birth_date = Column('birth_date', DateTime)
    phone_number = Column('phone_number',String(50),nullable=False)
    additional_data = Column('additional_data',String(150), nullable=False)





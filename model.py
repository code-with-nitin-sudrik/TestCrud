
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    name =Column(String)

    company_id=Column(Integer,ForeignKey('company.id'),nullable=True)
    age=Column(Integer,nullable=True)

    class Config:
        orm_mode=True

class Company(Base):
    __tablename__='company'
    id=Column(Integer,primary_key=True,autoincrement=True)
    email=Column(String,unique=True)
    location=Column(String)


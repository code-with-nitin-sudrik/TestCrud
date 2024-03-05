# coding: utf-8
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True, server_default=text("nextval('company_id_seq'::regclass)"))
    email = Column(String, unique=True)
    location = Column(String)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True, server_default=text("nextval('user_id_seq'::regclass)"))
    email = Column(String, unique=True)
    password = Column(String)
    is_active = Column(Boolean)
    name = Column(String)
    company_id = Column(ForeignKey('company.id'))
    age = Column(Integer)
    lastName = Column(String)

    company = relationship('Company')

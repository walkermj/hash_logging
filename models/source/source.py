# coding: utf-8
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True, server_default=text("nextval('company_id_seq'::regclass)"))
    name = Column(String(300))
    sdate = Column(String(300))
    email = Column(String(300))
    domain = Column(String(300))
    city = Column(String(300))


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, server_default=text("nextval('customer_id_seq'::regclass)"))
    name = Column(String(300))
    lastname = Column(String(300))
    address = Column(String(300))
    country = Column(String(300))
    city = Column(String(300))
    registry_date = Column(String(300))
    birthdate = Column(String(300))
    email = Column(String(300))
    phone_number = Column(String(300))
    locale = Column(String(300))


class DetailedRegistration(Base):
    __tablename__ = 'detailed_registration'

    id = Column(Integer, primary_key=True, server_default=text("nextval('detailed_registration_id_seq'::regclass)"))
    email = Column(String(300))
    password = Column(String(300))
    lastname = Column(String(300))
    name = Column(String(300))
    adress = Column(String(300))
    phone = Column(String(300))


class SimpleRegistration(Base):
    __tablename__ = 'simple_registration'

    id = Column(Integer, primary_key=True, server_default=text("nextval('simple_registration_id_seq'::regclass)"))
    email = Column(String(300))
    password = Column(String(300))


class UserAgent(Base):
    __tablename__ = 'user_agent'

    id = Column(Integer, primary_key=True, server_default=text("nextval('user_agent_id_seq'::regclass)"))
    ip = Column(String(300))
    countrycode = Column(String(300))
    useragent = Column(String(300))

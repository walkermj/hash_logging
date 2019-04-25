from sqlalchemy import create_engine, DDL, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base

from LocalConfig import db_connection_string

#Base declared first so can be used within the following module
Base = declarative_base()
from . import hash_log

def GetEngine():
    """Get an engine for the database as specified in the config"""
    return create_engine(db_connection_string, echo=True)

def GetSession():
    """Get a database session"""
    return sessionmaker(bind=GetEngine())

def CreateDatabase():
    """Create dest schema and table(s)"""

    engine = GetEngine()

    # create schema if doesn't exist
    event.listen(Base.metadata, 'before_create', DDL("CREATE SCHEMA IF NOT EXISTS dest"))
    # create all tables
    Base.metadata.create_all(GetEngine())

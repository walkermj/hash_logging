from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from LocalConfig import perftest_db_connection_string

#Base declared first so can be used within the following module
Base = declarative_base()
from . import source_tbls

def GetEngine():
    """Get an engine for the database as specified in the config"""
    return create_engine(perftest_db_connection_string, echo=True)

def GetSession():
    """Get a database session"""
    return sessionmaker(bind=GetEngine())




import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from . import Base

class hashLogTable(Base):
    __tablename__= 'hash_log'
    __table_args__ = ({"schema": "dest"})

    hash_value  = Column(String(128), primary_key=True)
    email       = Column(String(300), nullable=False)
    de_created  = Column(DateTime, default = datetime.datetime.utcnow)




from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table, Column, String, BigInteger, Integer, \
    DateTime, LargeBinary, Boolean, ForeignKey, create_engine, UniqueConstraint
from project import db


Base = declarative_base()

Base.query = db.session.query_property()

class DeviceMatrix(db.Model):
    __tablename__ = "devicematrix"
    id = Column(Integer, primary_key=True, autoincrement=True)
    devicetype = Column(String, unique=True)
    category = Column(String)
    description = Column(String)
    article = Column(String)
    jws = Column(Boolean)

    def __init__(self, devicetype, category, description, article, jws):
        self.devicetype = devicetype
        self.category = category
        self.description = description
        self.article = article
        self.jws = jws


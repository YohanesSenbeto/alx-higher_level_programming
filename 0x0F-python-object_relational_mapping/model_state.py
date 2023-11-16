#!/usr/bin/python3
"""
Define State class & create states table in a MySQL database.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

engine = create_engine("mysql://username:password@localhost/mydatabase")
Base.metadata.create_all(engine)

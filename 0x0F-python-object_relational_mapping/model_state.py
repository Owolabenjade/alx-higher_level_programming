#!/usr/bin/python3
"""
Module contains the class definition of a State and an instance Base.
This State class is a SQLAlchemy model that links to the table 'states'.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Represents a state for a MySQL database.
    __tablename__: Name of the table
    id: The state's id
    name: The name of the state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


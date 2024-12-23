#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of declarative_base
Base = declarative_base()


class State(Base):
    """
    Class definition of a State

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
    """
    __tablename__ = 'states'

    # Column for the state's id
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    
    # Column for the state's name
    name = Column(String(128), nullable=False)
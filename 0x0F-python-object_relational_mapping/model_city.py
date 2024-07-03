#!/usr/bin/python3
"""
This module defines the City class and links it to the cities table in
the database using SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State

class City(Base):
    """
    The City class corresponds to the cities table.
    Attributes:
        id (int): city id, primary key, autoincremented and not nullable.
        name (str): city name, not nullable.
        state_id (int): id of the state the city belongs to, not nullable, foreign key.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(256), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)


#!/usr/bin/python3
"""
Contains the class definition of a City
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """
    Class representing the cities table
    
    Attributes:
        id: The city's id
        name: The city's name
        state_id: The state id
    """
    __tablename__ = 'cities'
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
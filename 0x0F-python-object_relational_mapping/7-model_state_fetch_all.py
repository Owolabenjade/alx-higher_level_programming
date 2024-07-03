#!/usr/bin/python3
"""
This script lists all State objects from the database `hbtn_0e_6_usa`.
It uses SQLAlchemy to query the database and prints each state in the format: <state id>: <state name>.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
        # Create engine that connects to the MySQL database
        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}')
        # Bind the engine to the metadata of the Base class so that the
        # declaratives can be accessed through a DBSession instance
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        # A DBSession() instance establishes all conversations with the database
        # and represents a "staging zone" for all the objects loaded into the
        # database session object.
        session = DBSession()

        # Query all states in the database
        states = session.query(State).order_by(State.id).all()
        for state in states:
            print(f"{state.id}: {state.name}")

        session.close()


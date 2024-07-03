#!/usr/bin/python3
"""
This script adds the State object “Louisiana” to the database `hbtn_0e_6_usa`.
It uses SQLAlchemy to manage database transactions. After adding the state, it prints
the ID of the new state.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}')
        Base.metadata.bind = engine

        Session = sessionmaker(bind=engine)
        session = Session()

        # Create new State object
        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()  # Commit to save the new state to the database

        print(new_state.id)  # Print the ID of the new state

        session.close()


#!/usr/bin/python3
"""
This script deletes all State objects from the database `hbtn_0e_6_usa` that have
a name containing the letter 'a'. It uses SQLAlchemy to interact with the database
safely and efficiently.
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

        # Query for all states containing 'a' in their names
        states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
        for state in states_to_delete:
            session.delete(state)  # Delete each state object found

        session.commit()  # Commit changes to the database
        session.close()


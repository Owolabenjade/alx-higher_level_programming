#!/usr/bin/python3
"""
This script updates the name of the State object with an id of 2
to "New Mexico" in the database `hbtn_0e_6_usa` using SQLAlchemy.
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

        # Find the state with id = 2
        state = session.query(State).filter(State.id == 2).first()
        if state:
            state.name = "New Mexico"  # Change the name to "New Mexico"
            session.commit()  # Commit the change to the database

        session.close()


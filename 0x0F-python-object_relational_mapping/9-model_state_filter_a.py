#!/usr/bin/python3
"""
This script lists all State objects from the database `hbtn_0e_6_usa` that contain
the letter 'a' in their name. The results are sorted in ascending order by states.id.
It uses SQLAlchemy for querying the database.
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

        # Query all states containing 'a' in their names, ordered by id
        states = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
        for state in states:
            print(f"{state.id}: {state.name}")

        session.close()


#!/usr/bin/python3
"""
This script prints the first State object from the database `hbtn_0e_6_usa`.
It uses SQLAlchemy to connect to the database and queries only the first state by its id.
If the table is empty, it prints 'Nothing'.
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

        # Query the first state in the database, ordered by id
        state = session.query(State).order_by(State.id).first()
        if state:
            print(f"{state.id}: {state.name}")
        else:
            print("Nothing")

        session.close()


#!/usr/bin/python3
"""
This script prints the ID of a State object with the specified name from the
database `hbtn_0e_6_usa`. It uses SQLAlchemy to perform the query securely,
avoiding SQL injection. If no state with the given name is found, it displays 'Not found'.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) == 5:
        username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}')
        Base.metadata.bind = engine

        Session = sessionmaker(bind=engine)
        session = Session()

        # Query for the state with the specified name using a parameterized filter
        state = session.query(State).filter(State.name == state_name).first()
        if state:
            print(state.id)
        else:
            print("Not found")

        session.close()


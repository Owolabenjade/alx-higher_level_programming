#!/usr/bin/python3
"""
This script lists all State objects and their corresponding City objects from the database
`hbtn_0e_101_usa`. Each city is displayed under its state in ascending order by states.id
and cities.id using SQLAlchemy ORM.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}')
        Base.metadata.bind = engine

        Session = sessionmaker(bind=engine)
        session = Session()

        # Query all states and their corresponding cities
        states = session.query(State).order_by(State.id).all()
        for state in states:
            print(f"{state.id}: {state.name}")
            for city in sorted(state.cities, key=lambda x: x.id):
                print(f"\t{city.id}: {city.name}")

        session.close()


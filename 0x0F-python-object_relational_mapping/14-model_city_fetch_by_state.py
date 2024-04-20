#!/usr/bin/python3
"""
This script lists all City objects from the database `hbtn_0e_14_usa`. Each city is
printed alongside its corresponding state name, formatted as "<state name>: (<city id>) <city name>".
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}')
        Base.metadata.bind = engine

        Session = sessionmaker(bind=engine)
        session = Session()

        # Query for all cities with their states
        cities = session.query(City, State).join(State).order_by(City.id).all()
        for city, state in cities:
            print(f"{state.name}: ({city.id}) {city.name}")

        session.close()


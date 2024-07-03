#!/usr/bin/python3
"""
This script lists all City objects from the database `hbtn_0e_101_usa`.
Each city's information is displayed along with the state it belongs to.
The information is formatted as '<city id>: <city name> -> <state name>'.
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

        # Query all cities and join with states to fetch the related state information in one go
        cities = session.query(City).order_by(City.id).all()
        for city in cities:
            print(f"{city.id}: {city.name} -> {city.state.name}")

        session.close()


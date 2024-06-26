#!/usr/bin/python3
"""
This script creates a State "California" with a City "San Francisco"
in the database `hbtn_0e_100_usa` using SQLAlchemy.
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
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        # Create new State and City
        new_state = State(name="California")
        new_city = City(name="San Francisco", state=new_state)
        session.add(new_state)
        session.add(new_city)
        session.commit()

        print(f"{new_state.id} {new_state.name}")
        print(f"{new_city.id} {new_city.name}")

        session.close()


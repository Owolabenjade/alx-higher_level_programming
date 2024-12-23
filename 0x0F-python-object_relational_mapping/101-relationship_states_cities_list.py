#!/usr/bin/python3
"""
Script that lists all State objects and corresponding City objects
from the database hbtn_0e_101_usa
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus


if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    username = sys.argv[1]
    password = quote_plus(sys.argv[2])
    database = sys.argv[3]
    
    # Create connection to database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )
    
    # Create session factory
    Session = sessionmaker(bind=engine)
    
    # Create session
    session = Session()
    
    # Query all State objects and their associated City objects
    # Using one query with the cities relationship
    states = session.query(State).order_by(State.id).all()
    
    # Display results
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in sorted(state.cities, key=lambda x: x.id):
            print(f"    {city.id}: {city.name}")
    
    # Close session
    session.close()
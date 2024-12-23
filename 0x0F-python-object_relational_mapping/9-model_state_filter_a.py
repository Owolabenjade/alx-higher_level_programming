#!/usr/bin/python3
"""
Script that lists all State objects containing letter 'a'
from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus


if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    username = sys.argv[1]
    password = quote_plus(sys.argv[2])  # Encode special characters in password
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
    
    # Query all State objects containing letter 'a', ordered by id
    states = session.query(State)\
                   .filter(State.name.like('%a%'))\
                   .order_by(State.id)\
                   .all()
    
    # Display results
    for state in states:
        print("{}: {}".format(state.id, state.name))
    
    # Close session
    session.close()
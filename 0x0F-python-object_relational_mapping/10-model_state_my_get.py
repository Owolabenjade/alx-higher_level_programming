#!/usr/bin/python3
"""
Script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus


if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    username = sys.argv[1]
    password = quote_plus(sys.argv[2])
    database = sys.argv[3]
    state_name = sys.argv[4]  # State name to search for
    
    # Create connection to database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )
    
    # Create session factory
    Session = sessionmaker(bind=engine)
    
    # Create session
    session = Session()
    
    # Query the State object with the given name
    state = session.query(State)\
                  .filter(State.name == state_name)\
                  .first()
    
    # Display result
    if state:
        print(state.id)
    else:
        print("Not found")
    
    # Close session
    session.close()
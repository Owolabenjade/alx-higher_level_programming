#!/usr/bin/python3
"""
Script that adds the State object "Louisiana"
to the database hbtn_0e_6_usa
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
    
    # Create connection to database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )
    
    # Create session factory
    Session = sessionmaker(bind=engine)
    
    # Create session
    session = Session()
    
    # Create new State object
    new_state = State(name="Louisiana")
    
    # Add the new state to the session
    session.add(new_state)
    
    # Commit the session to persist the changes
    session.commit()
    
    # Print the new state's id
    print(new_state.id)
    
    # Close session
    session.close()
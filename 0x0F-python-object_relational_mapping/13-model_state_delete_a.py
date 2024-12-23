#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing
the letter 'a' from the database hbtn_0e_6_usa
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
    
    # Query all State objects containing letter 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    
    # Delete the states
    for state in states_to_delete:
        session.delete(state)
    
    # Commit the changes
    session.commit()
    
    # Close session
    session.close()
#!/usr/bin/python3
"""
Script that creates the State "California" with the City "San Francisco"
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
    
    # Create all tables in the database
    Base.metadata.create_all(engine)
    
    # Create session factory
    Session = sessionmaker(bind=engine)
    
    # Create session
    session = Session()
    
    # Create new State "California"
    california = State(name="California")
    
    # Create new City "San Francisco"
    san_francisco = City(name="San Francisco")
    
    # Add city to state's cities collection
    california.cities.append(san_francisco)
    
    # Add state to session (city will be added automatically via cascade)
    session.add(california)
    
    # Commit session to persist changes
    session.commit()
    
    # Close session
    session.close()
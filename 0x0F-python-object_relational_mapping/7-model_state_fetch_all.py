#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus


if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Create the connection string
    username = sys.argv[1]
    password = quote_plus(sys.argv[2])
    database = sys.argv[3]
    
    # Create engine that connects to the MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database
        )
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    try:
        # Query all State objects and sort by id
        states = session.query(State).order_by(State.id).all()

        # Display results
        for state in states:
            print("{}: {}".format(state.id, state.name))

    except Exception as e:
        print("Error occurred:", e)

    finally:
        # Close the session
        session.close()
#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote


if __name__ == "__main__":
    # Get MySQL username, password and database name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = quote(sys.argv[2])  # URL-encode the password
    database_name = sys.argv[3]

    # Create database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                         .format(mysql_username, mysql_password, database_name))

    # Create session maker
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query first State object
    first_state = session.query(State).order_by(State.id).first()

    # Print the result
    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    # Close session
    session.close()


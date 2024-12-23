#!/usr/bin/python3
"""
Script that starts link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from urllib.parse import quote_plus

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Create engine that connects to the MySQL server
    # Using quote_plus to properly encode special characters in password
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            quote_plus(sys.argv[2]),
            sys.argv[3]
        )
    )

    # Create all tables in the database
    Base.metadata.create_all(engine)
#!/usr/bin/python3
"""
Start link class to table in database by creating an engine and
creating all tables stored in this module's Base metadata.
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    # Usage: 6-model_state.py <mysql username> <mysql password> <database name>
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}', pool_pre_ping=True)
        Base.metadata.create_all(engine)


#!/usr/bin/python3
"""
This module provides a script that connects to a MySQL database and lists all states
from the database `hbtn_0e_0_usa` where the name exactly matches the user input.
The comparison is case-sensitive, and the results are sorted by the state ids.
"""

import MySQLdb
import sys

def filter_states(username, password, dbname, state_name):
    """
    Connects to a MySQL database and lists all states where the name matches
    the state_name argument, sorted by id.
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=dbname)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 5:
        filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


#!/usr/bin/python3
"""
This module provides a script that connects to a MySQL database and safely lists all
states from the database `hbtn_0e_0_usa` where the name matches the user-provided input.
This implementation uses parameterized queries to avoid SQL injection.
"""

import MySQLdb
import sys

def safe_filter_states(username, password, dbname, state_name):
    """
    Connects to a MySQL database and safely lists all states where the name matches
    the state_name argument, sorted by id. This function uses parameterized queries
    to prevent SQL injection.
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
        safe_filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


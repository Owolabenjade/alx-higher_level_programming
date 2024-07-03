#!/usr/bin/python3
"""
This module provides a script that connects to a MySQL database and lists all cities
from a specified state in the database `hbtn_0e_4_usa`. The list is sorted by city id
and the script uses parameterized queries to ensure it is safe from SQL injections.
"""

import MySQLdb
import sys

def list_cities_in_state(username, password, dbname, state_name):
    """
    Connects to a MySQL database and lists all cities from a specified state,
    sorted by city id. The input state name is safely incorporated into the query
    using parameterized statements to prevent SQL injection.
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=dbname)
    cur = db.cursor()
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 5:
        list_cities_in_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


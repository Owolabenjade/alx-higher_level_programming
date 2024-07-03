#!/usr/bin/python3
"""
This module provides a script that connects to a MySQL database and lists all cities
from the database `hbtn_0e_4_usa`. Each city is listed with its corresponding state,
sorted by city id in ascending order. The script ensures data integrity and is safe from
SQL injection by using parameterized queries.
"""

import MySQLdb
import sys

def list_cities(username, password, dbname):
    """
    Connects to a MySQL database and lists all cities along with their associated state,
    sorted by city id. This function uses parameterized queries to ensure safety and
    performance.
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=dbname)
    cur = db.cursor()
    cur.execute("""
        SELECT cities.id, cities.name, states.name 
        FROM cities 
        JOIN states ON cities.state_id = states.id 
        ORDER BY cities.id ASC
    """)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_cities(sys.argv[1], sys.argv[2], sys.argv[3])


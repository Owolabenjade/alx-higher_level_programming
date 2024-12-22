#!/usr/bin/python3
"""
Script that lists all states with a name starting with N
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL connection parameters from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Establish connection to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object to execute queries
        cursor = db.cursor()

        # Execute the SELECT query to get states starting with N
        cursor.execute("""
            SELECT * FROM states 
            WHERE name LIKE 'N%'
            ORDER BY id ASC
        """)

        # Fetch all rows from the query result
        states = cursor.fetchall()

        # Display the results
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)

    finally:
        # Close cursor and database connection
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()
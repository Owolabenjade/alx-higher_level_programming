#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb


def list_cities_by_state(username, password, database, state_name):
    """
    Lists all cities of a given state from the database hbtn_0e_4_usa.
    
    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): Database name
        state_name (str): Name of the state to search for
    """
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object
        cursor = db.cursor()

        # Create the SQL query using parameterized query to prevent SQL injection
        query = """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
        """

        # Execute the query with the state name as parameter
        cursor.execute(query, (state_name,))

        # Fetch all the rows
        rows = cursor.fetchall()

        # Print the cities
        print(", ".join(city[0] for city in rows))

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close cursor and database connection
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the main function
    list_cities_by_state(username, password, database, state_name)

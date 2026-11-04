#!/usr/bin/python3
"""Lists states matching a name supplied as an argument."""

import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor
    cur = db.cursor()

    # Get the state name from command-line argument
    state_name = sys.argv[4]

    # Execute SQL query using format()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    # Fetch and display results
    rows = cur.fetchall()

    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()

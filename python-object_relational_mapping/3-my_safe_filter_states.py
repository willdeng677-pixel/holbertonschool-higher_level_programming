#!/usr/bin/python3
"""Lists states matching a name safely."""

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

    # Get state name from command-line argument
    state_name = sys.argv[4]

    # Execute a parameterized SQL query
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (state_name,)
    )

    # Fetch and display results
    rows = cur.fetchall()

    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()

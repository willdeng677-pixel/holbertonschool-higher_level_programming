#!/usr/bin/python3
"""Lists states with names starting with N."""

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

    # Execute SQL query
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )

    # Fetch and print results
    rows = cur.fetchall()

    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()

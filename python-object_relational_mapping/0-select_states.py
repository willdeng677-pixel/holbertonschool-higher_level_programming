#!/usr/bin/env python3
"""Lists all states from the database hbtn_0e_0_usa."""

import MySQLdb
import sys


def main():
    """Connect to MySQL and list all states."""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3
        ]
    )

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()

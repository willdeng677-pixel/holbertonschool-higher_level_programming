#!/usr/bin/env python3
"""List all states from a MySQL database."""

import MySQLdb
import sys

conn = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3],
    charset="utf8"
)

cur = conn.cursor()

cur.execute("SELECT * FROM states ORDER BY id ASC")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()

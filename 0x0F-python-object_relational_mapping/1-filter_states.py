#!/usr/bin/python3
"""lists all states with a name starting with N"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], database=argv[3], charset="utf8")

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for rows in query_rows:
        if rows[1].startswith("N"):
            print(rows)
    cur.close()
    conn.close()

#!/usr/bin/python3
"""lists all states with a name starting with N"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], database=argv[3], charset="utf8")

    cur = conn.cursor()
    query_in = """
    SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    query_in = query_in.format(argv[4])
    cur.execute(query_in)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

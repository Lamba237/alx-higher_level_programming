#!/usr/bin/python3
"""lists all cities from the database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")

    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "ORDER BY cities.id ASC")
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    conn.close()

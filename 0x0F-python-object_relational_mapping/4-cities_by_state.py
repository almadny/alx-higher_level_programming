#!/usr/bin/python3
""" Python connection to a database using mysqldb connector """

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    try:
        conn = MySQLdb.connect(
            host="localhost", port=3306,
            user=username, passwd=password, db=dbname, charset="utf8")
    except Exception as e:
        print(e)
    else:
        cur = conn.cursor()
        cur.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities\
                    INNER JOIN states\
                    ON cities.state_id = states.id")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        conn.close()

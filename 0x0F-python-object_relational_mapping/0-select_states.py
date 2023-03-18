#!/usr/bin/python3
""" Python connection to a database using mysqldb connector """

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
dbname = sys.argv[3]
conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname, charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM hbtn_0e_0_usa.states ORDER BY states.id")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()

if __name__ == "__main__":

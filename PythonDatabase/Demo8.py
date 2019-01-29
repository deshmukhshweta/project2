# WAP to read all rows and cols

import sqlite3 as sql
conn = sql.connect("student_info.db")
curs = conn.cursor()
c = curs.execute("select * from student")
lis = c.fetchall()
print(lis)
res = c.fetchone()
print(res)
print(type(res))

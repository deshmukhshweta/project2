# WAP to read all rows and cols

import sqlite3 as sql
conn = sql.connect("student_info.db")
curs = conn.cursor()
c = curs.execute("select contact,idno from student")

for x in c:
    print(x)

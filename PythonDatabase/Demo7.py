# to read all rows and cols

import sqlite3 as sql
conn = sql.connect("student_info.db")
curs = conn.cursor()
c = curs.execute("select * from student")
lis = c.fetchall()

for x in lis:
    print(x)

print("---------------------")

for x in lis:
    print(x[0],x[1],x[2])
    

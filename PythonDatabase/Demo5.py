#inserting Multi values at a time
import sqlite3 as sql
conn = sql.connect("student_info.db")
curs = conn.cursor()
val = [
    (104,'AAA',9874561230),
    (105,'BBB',9874561231),
    (106,'CCC',9874561232),
    (107,'DDD',9874561233),
    (108,'EEE',9874561234)
    ]
curs.executemany("insert into student values(?,?,?)",val)
conn.commit()
conn.close()
print("Data Saved")

#create table
import sqlite3 as sql
conn = sql.connect("student_info.db")
curs = conn.cursor()
try:
    curs.execute("create table student(idno number primary key,name text,contact number)")
    print("Table Created")
except sql.OperationalError:
    print("Table is Available")

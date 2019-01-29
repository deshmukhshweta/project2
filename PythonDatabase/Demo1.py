import sqlite3
conn = sqlite3.connect("student_info.db")
curs = conn.cursor()
print(type(curs))

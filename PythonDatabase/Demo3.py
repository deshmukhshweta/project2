# insert data into student table
import sqlite3 as sql
conn = sql.connect("student_info.db")
curs = conn.cursor()
try:
    curs.execute("insert into student values(101,'Ravi',9876543210)")
    print("Data Saved")
except sql.IntegrityError:
    print("Please Change Idno")
finally:
    conn.commit() # Save
    conn.close()
    

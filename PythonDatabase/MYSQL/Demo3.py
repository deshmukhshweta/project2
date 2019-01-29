#creating database using python in MySQL
import mysql.connector as my
conn = my.connect(user="root",password="root",host="127.0.0.1",database="sathya")
if conn.is_connected():
    print("Connected to Sathya Database")
    curs = conn.cursor()
    curs.execute("create table employee(idno integer(4),name varchar(50),salary integer(7),contact integer(10))")
    print("Employee Table is Created") 
    conn.commit()
    conn.close()
else:
    print("Not Connected")


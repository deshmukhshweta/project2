#creating database using python in MySQL
import mysql.connector as my
conn = my.connect(user="root",password="root",host="127.0.0.1")
if conn.is_connected():
    print("Connected to MYSQL")
    curs = conn.cursor()
    curs.execute("create database sathya")
    print("Sathya Database is Created")    
    conn.commit()
    conn.close()
else:
    print("Not Connected")


#Making a Connecton to MYSQL "sathya" Database

import mysql.connector as my

def my_db_connector():
    conn = my.connect(user="root",password="root",host="127.0.0.1",database="sathya")
    return conn


def my_db_insertion(idno,name,salary,cno):
    conn = my_db_connector()
    curs = conn.cursor()
    tup = (idno,name,salary,cno)
    print(type(tup))
    curs.execute("insert into employee (idno,name,salary,contact) values(%s,%s,%s,%s)",tup)
    conn.commit()
    conn.close()
    print("Employee Created")
    
    

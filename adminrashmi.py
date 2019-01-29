import sqlite3 as sql
conn=sql.connect("admin.db")
curs=conn.cursor()
#curs.execute("create table admin(password number)")1st
#print("table is created")1st
#curs.execute("insert into admin values(12345)")2nd
#print ("data saved")2nd
print("1.Admin")
print("2.Account_Holder")
a=int(input("select any one option"))
if(a==1):
    print("welcome admin")
    pw=int(input("enter password:"))
    a=curs.execute("select password from admin")
    pd=a.fetchone()
    if(pw==pd[0]):
           print("admin login successfully")
           print("1.add account holder")
           print("2.delete account holder")
           print("3.view all")
           print("4.exit")
           a1=int(input("enter any one option"))
           if(a1==1):
              print("add details in acc_holder")
           #   curs.execute("create table acc_holder(name text,acc_no number primary key ,password number)")
           #   print("table is created")
           #   curs.execute("insert into acc_holder values('Rasmhi bathre',23477788899,882793)")
           #   print("data saved")
           #   conn.commit()      



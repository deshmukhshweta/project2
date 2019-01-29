import SathyaConnector as sathya

idno = int(input("Idno : "))
name = input("Name : ")
salary = int(input("Salary : "))
cno = int(input("Contact No : "))

conn = sathya.my_db_connector()
curs = conn.cursor()
curs.execute("insert into employee(idno,name,salary,contact) values(%s,%s,%s,%s)",(idno,name,salary,cno))
print("Employee Added")
conn.commit()
conn.close()

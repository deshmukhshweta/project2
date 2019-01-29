import mysql.connector as my
conn = my.connect(user="root",password="root",database="sathya",host="127.0.0.1")
if conn.is_connected():
    print("Connected")
    curs = conn.cursor()
    curs.execute("select * from employee")
    li = curs.fetchall()
    for x in li:
        print(x)


    idno = int(input("Enter IDNO : "))
    for y in li:
        if(y[0] == idno):
            print(y)
            break
    else:
        print("Wrong Idno")
        
    

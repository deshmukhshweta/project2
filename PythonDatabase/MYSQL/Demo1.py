import mysql.connector as my
try:
    conn = my.connect(user="root",password="root",host="127.0.0.1",database="student_info")
    if conn.is_connected():
        print("Connected to Student Info Database")
        curs = conn.cursor()
        res = curs.execute("insert into student values(101,'Ravi',78945)")
        print(res)
        conn.commit()
        conn.close()
    else:
        print("Sorry Not Connected")

except my.errors.ProgrammingError:
    print("Database not Found")

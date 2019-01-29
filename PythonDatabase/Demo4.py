# Read data from user and insert into database
import sqlite3 as sql

def readInput():
    ''' This function will read input from user and return all values in tuple'''
    idno = int(input("IDNO : "))
    name = input("Name : ")
    cno = int(input("Contact No : "))
    return idno,name,cno

def insertIntoDB():
    conn = sql.connect("student_info.db")
    curs = conn.cursor()
    result = readInput()
    try:
        curs.execute("insert into student values(?,?,?)",result)
        print("Data Saved")
    except sql.IntegrityError:
        print("Change IDNO ")
    finally:
        conn.commit()
        conn.close()


insertIntoDB()






        


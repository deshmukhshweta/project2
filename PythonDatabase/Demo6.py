#program to insert idno only

import sqlite3 as sql

def readInput():
    idno = int(input("IDNO : "))
    return idno

def insertIntoDB():
    conn = sql.connect("student_info.db")
    curs = conn.cursor()
    result = readInput()
    curs.execute("insert into student(idno) values(?)",(result,))
    conn.commit()
    conn.close()
    print("IDNO Saved")

insertIntoDB()

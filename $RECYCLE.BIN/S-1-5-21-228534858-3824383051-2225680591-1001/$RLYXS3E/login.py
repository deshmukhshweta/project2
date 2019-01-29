import sqlite3 as sql
def login():
    uname=input("please enter username:")
    pw=int(input("please enter passwaord:"))
    with sql.connect("admin_table.db")as ad:
         curs=ad.cursor()
         user=("select*from admin_user where uname=? AND pas=?")
         curs.execute(user,[(uname),(pw)])
         result=curs.fetchone()
         if result:
            for i in results:
                print("welcome"+i[2])
                break
         else:
            print("username and password is incorrect")
            ans=input("do you want to continue no:")
            if (ans=="no"):
               print("account is blocked")
            #break
login()        
           

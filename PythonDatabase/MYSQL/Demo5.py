import SathyaConnector as sathya

i = int(input("IDNO : "))
n = input("Name : ")
s = int(input("Salary : "))
c = int(input("Contact : "))

sathya.my_db_insertion(i,n,s,c)

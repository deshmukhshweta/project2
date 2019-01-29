
idno = input("IDNO : ")
password = input("Password : ")

from firebase import firebase as fb

fire = fb.FirebaseApplication("https://merchant-application-e1450.firebaseio.com/merchant/employee/stocker",None)
result = fire.get("stocker",idno)
if result != None:
    if result["password"] == password:
        print(result)
    else:
        print("Invalid Password")
else:
    print("Invalid Idno")


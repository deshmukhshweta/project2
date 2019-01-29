
idno = int(input("IDNO"))
from firebase import firebase as fb
fire = fb.FirebaseApplication("https://merchant-application-e1450.firebaseio.com/merchant/employee/stocker",None)
result = fire.get("stocker",idno)
print(result)

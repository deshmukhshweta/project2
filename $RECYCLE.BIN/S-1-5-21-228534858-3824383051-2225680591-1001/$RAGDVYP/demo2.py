from firebase import  firebase as fb
fire=fb.FirebaseApplication("https://rashmi-1995.firebaseio.com/",None)
result=fire.put('Information',"personal details",{"Qualification":"B.E(electronic & communication","Age":"22","C_NO":"9770535567","Name":"Vikas Singore"})
print(result)

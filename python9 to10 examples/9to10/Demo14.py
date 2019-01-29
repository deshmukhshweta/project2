d1 = {1:"A",2:"B",3:"C"}
print("Items in Dict :",d1)
d1.clear()
print("Items in Dict :",d1)
#------------------

d1 = {1:"A",2:"B",3:"C"}
print("Items in D1 :",d1)
d2 = d1.copy()
print("Items in D2 :",d2)

#----------------------
d1 = {1:"A",2:"B",3:"C"}
value = d1.get(1)
print(value,type(value))

#-----------------------
d1 = {1:"A",2:"B",3:"C"}
d2 = d1.items()
print(d2,type(d2))

#-----------------------
d1 = {1:"A",2:"B",3:"C"}
keys = d1.keys()
print(keys, type(keys))

#-----------------------
d1 = {1:"A",2:"B",3:"C"}
values = d1.values()
print(values,type(values))

#-----------------------
d1 = {1:"A",2:"B",3:"C"}
val = d1.pop(2)
print(d1)
print(val)









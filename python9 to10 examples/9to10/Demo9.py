#Working With Open Functions
t1 = (10,20,30,40,50)
print(sum(t1))
print(max(t1))
print(min(t1))
print(len(t1))


t2 = "sathya",10.25,100 # packing
print(t2)
print(type(t2))

a,b,c = t2 #Un Packing
print(a)# sathya  a type 'str'
print(b)# 10.25  b type 'float'
print(c)# 100 c type 'int'


t3 = ()#Empty tuple
print(type(t3))

t4 = ("sathya")
print(type(t4))# type 'str'
#Note : 

t4 = ("sathya",)
print(type(t4))# type 'tuple'


t5 = (10,55,-5,14,14.25)
result = sorted(t5)
print(result)
print(type(result))

t5 = (10,55,-5,14,14.25)
print(all(t5))

t6 = (True,True,True)
print(all(t6))

t7 = ()
print(all(t7))


t1 = ("sathya",10.326,100,"sathya")
no = t1.count("sathya")
print(no)
pos = t1.index("sathya")
print(pos)


print("sathya" in t1)
print(45 in t1)
print("Naveen" not in t1)
print("sathya" not in t1)








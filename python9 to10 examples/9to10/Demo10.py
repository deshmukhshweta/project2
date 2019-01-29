s1 = {}# no
print(type(s1)) # dict

s1 = set()# Yes
print(type(s1)) # set


s1 = {1,2,3,4,5}
print(s1)
# 'set' object does not support indexing
# print(s1[0]) Error
# print(s1[0:3]) Error

s2 = {10,20,30,40,50,10,20}
print(s2)

s3 = {"A","B","C","D","B","A"}
print(s3)

s4 = {True,False,False}
print(s4)



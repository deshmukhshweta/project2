s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s3 = s1.difference(s2)
print(s3)

s4 = s2.difference(s1)
print(s4)

s5 = s1.intersection(s2)
print(s5)

s = {1,2,3,4,5}
s6 = s.pop() # removes arbitrary element
# arbitrary means based on random choice
print(s6,type(s6))
print(s)


s1 = {1,2,3,4,5}
print(s1)
s2 = s1.remove(3)
print(s2,type(s2))
print(s1)
# s3 = s1.remove(90)KeyError: 90
#print(s3)



s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1.union(s2)
print(s3,type(s3))


s1.update(s2)
print(s1)
print(s2)
















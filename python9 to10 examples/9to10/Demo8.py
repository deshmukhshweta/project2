t1 = () # Empty Tuple
print(t1) # ()
print(type(t1)) # <class 'tuple'>


t2 = ("samsung",12500.45,2016)
print(t2)
print(t2[0])
print(t2[0:2])
print(t2[-1])
print(t2[0:2:2])

#Working With '+' and '*' Operators
t1 = (10,20,30)
t2 = (40,50,60)
t3 = t1+t2 # Will add 2 Tuples and return new Tuple
print(t3)
print(id(t1))
print(id(t2))
print(id(t3))

t4 = t1*3 # Will Multi the Tuple with given number
          # and return new tuple
print(t4)






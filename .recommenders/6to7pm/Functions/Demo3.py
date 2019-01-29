# In a function defination we can call other function
# ===================================================

def one():
    two()
    print("I am One")

def three():
    print("I am Three")    

def two():
    print("I am Two")
    three()


print("Hi")
one()
three()
print("bye")



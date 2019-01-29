# In a function defination we can call other function
# ===================================================
def one():
    print("I am one")

def two():
    print(one())
    print("I am Two")

def three():
    print("I am three")
    two()
    print("3 Again")

def four():
    print(three())
    print("Bye")

one()
four()
three()




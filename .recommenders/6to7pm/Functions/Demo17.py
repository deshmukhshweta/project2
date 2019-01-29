def fun1(name=None,age=0):
    print("Welcome Mr/Miss : ",name)
    if(age>=23):
        print(age," is Valid Age")
    else:
        print(age," is Invalid Age")

# in this function call function will take default values
fun1()

# in this function call "Ravi" is assign to name and age is 0
fun1("Ravi")

# in this function call 45 is assign to name and age is 0
fun1(45)

# in this function call 45 is assign to age and name is None
fun1(age=45)

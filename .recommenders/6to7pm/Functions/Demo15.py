def fun1(name,age):
    print("Welcome Mr/Miss : ",name)
    if(age>=23):
        print(age," is Valid Age")
    else:
        print(age," is Invalid Age")

fun1("Ravi",23)

fun1(24,25)

# fun1(24,"Ravi") Error

# fun1() # fun1() missing 2 required positional arguments

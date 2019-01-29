#WAP to read 2 no's from user and print big no or same
no1 = int(input("Enter 1st no: "))
no2 = int(input("Enter 2nd no: "))

if(no1==no2):
    print("Both are same")
elif(no1 > no2):
    print(no1,"is big")
else:
    print(no2,"is big")
print("Thanks")
          

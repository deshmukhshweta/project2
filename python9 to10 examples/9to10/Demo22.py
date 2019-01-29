#WAP for ATM Process
#Validate Pin No
#Allow the User to Withdraw
#Allow the User to Balance Check

balance = 10000.00
pin_no = int(input("Enter Pin No : "))
if(pin_no == 5475):
    print("Welcome to Sathya ATM")
    print("1. Withdraw")
    print("2. Balance Check")
    option = int(input("Select One Option :"))
    if(option == 1):
        amount = int(input("Enter Amount :"))
        if(amount%100 == 0):
            if(amount <= balance):
                balance = balance - amount
                print("Amount Withdrawl")
                print("Balance = ",balance)
            else:
                print("No Funds")
        else:
            print("Invalid Amount")
    elif(0
        print("Balance = ",balance)
    else:
        print("Invalid Option")
else:
    print("Invalid Pin No")
print("Thanks For Using Sathya ATM")
    

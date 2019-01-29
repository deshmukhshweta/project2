#WAP for ATM Process
#Validate Pin No
#Allow the User to Withdraw
#Allow the User to Balance Check
#Allow the User for 3 Attempts

balance = 10000.00
for x in range(3):
    pin = int(input("Enter Pin No : "))
    if(pin == 5475):
        print("Welcome To My ATM")
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
        elif(option == 2):
            print("Balance = ",balance)
        else:
            print("Invalid Option")
        break
    else:
        print("Invalid Pin No :")
        if(x == 2):
            print("Your Account is Blocked")
            print("Please Contact Home Branch")
            print("Thanks For Using ATM")
            break
        else:
            ans = int(input("To Continue Press 1 :"))
            if(ans == 1):
                continue
            else:
                break
print("Thanks")

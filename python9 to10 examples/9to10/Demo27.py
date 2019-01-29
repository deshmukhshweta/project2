#WAP to Display 1 to 10

x = 1
while(x <= 10):
    print(x)
    x = x+1 #x+=1

print("Thanks")


#-------------------------
no = int(input("Enter any no : "))
rev = 0
while(no != 0):
    rem = no%10
    no = no/10
    rev = (rev*10)+rem

print(rev)











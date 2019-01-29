#WAP to read a table no from user and print the table


tno = int(input("Enter Table No : "))
start = int(input("Enter From : "))
end = int(input("Enter To : "))

if(start>end):
    for x in range(start,(end-1),-1):
         print(tno," X ",x," = ",(tno*x))
else:
    for x in range(start,(end+1)):
        print(tno," X ",x," = ",(tno*x))
        
print("Thanks")
input()
    
               

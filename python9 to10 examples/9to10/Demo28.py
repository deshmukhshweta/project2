# Sum of Given No
# 23  2+3 = 5
# 1234  1 + 2 + 3 + 4 = 10

no = int(input("Enter a No : "))
sum = 0
while(no != 0):
    rem = no%10
    sum = sum + rem
    no = no/10
else:
    print("The sum = ",sum)
print("Thanks")


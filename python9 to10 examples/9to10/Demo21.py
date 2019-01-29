#WAP to read 3 subject marsk
# print Total and Average
# print Hig and Low marks
# Print pass in what and Fail in What

s1 = int(input("Enter 1st Sub Marks : "))
s2 = int(input("Enter 2nd Sub Marks : "))
s3 = int(input("Enter 3rd Sub Marks : "))

total = s1+s2+s3
average = total/3

print("Total Marks = ",total)
print("Average     = ",average)

if(s1>s2  and  s1>s3):
    print("The sub 1 is Hig")
else:
    print("The Sub 1 is Low")

if(s2>s1 and s2>s3):
    print("The Sub 2 is Hig")
else:
    print("The Sub 2 is Low")
    
if(s3>s1 and s3>s2):
    print("The Sub 3 is Hig")
else:
    print("The sub 3 is Low")      


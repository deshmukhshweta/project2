#Snippet to Open a File in read 
try:
    f = open("sample.txt")
    s = f.readline()
    print(s)
    s1 = f.readline()
    print(s1)
    f.close()
except FileNotFoundError:
    print("File Not Found")
print("Thanks")
    
#--------------------------------------
# Using loop and using readlines
try:
    f = open("sample.txt")
    for x in f.readlines():
        print(x)   
    f.close()
except FileNotFoundError:
    print("File Not Found")
print("Thanks")
    
#---------------------------------
# using read(number)
try:
    f = open("sample.txt")
    s = f.read(15)
    print(s)
    f.close()
except FileNotFoundError:
    print("File Not Found")
print("Thanks")

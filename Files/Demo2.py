#Snippet to Open a File in read mode and Reading whole data from file
try:
    f = open("sample.txt")
    s = f.read()
    print(s)
    s1 = f.read()#return empty String
    print(s1)# Print Nothing
    f.close()
except FileNotFoundError:
    print("File Not Found")
print("Thanks")
    

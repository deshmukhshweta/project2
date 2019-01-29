#Rading a File From a Path
try:
    f = open(r"C:\Users\Naveen\Desktop\soup.txt")
    s = f.read()
    print(s)
except FileNotFoundError:
    print("File not Found")

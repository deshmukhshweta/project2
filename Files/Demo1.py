#Snippet to open a File in Read mode
# Note: Default mode is "r" -- read
try:
    f = open("sample.txt")
    print(f)
except FileNotFoundError:
    print("File Not Found")

print("Thanks")

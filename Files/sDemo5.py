#working with "w"
try:
    f = open("Demo.txt","w")
    #print(f)
    f.write("****Hello Wolrd This is Demo****")
    print("Writing to File")
    f.close()
except FileNotFoundError:
    print("File Not Found")
print("Thanks")

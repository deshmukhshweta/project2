#working with "a"
try:
    f = open("Demo.txt","a")
    #print(f)
    f.write("ILM runs a batch processing environment capable of modeling, rendering and compositing tens of thousands of motion picture frames per day. Thousands of machines running Linux, IRIX, Compaq Tru64, OS X, Solaris, and Windows join together to provide a production pipeline used by ~800 users daily. Speed of development is key, and Python was a faster way to code (and re-code) the programs that control this production pipeline.")
    print("Writing to File")
    f.close()
except FileNotFoundError:
    print("File Not Found")
print("Thanks")

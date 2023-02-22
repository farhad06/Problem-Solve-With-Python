#open a file
f=open("text.txt","r")
print(f.read())

with open("text.txt","r") as f:
    for i in f:
        print(i)
#write a file
'''f=open("file.txt",'x')
f.write("This is a file")
f.close()'''
with open("new.txt","w") as f:
    f.write("This is a file written using withopen")
#delete a file
import os
os.remove("file.txt")

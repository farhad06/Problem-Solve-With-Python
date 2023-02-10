def calculateSum(string):
    s=0
    num=0
    for i in string:
        if i>='0' and i<='9':
            num=num*10+int(i)
        else:
            s=s+num
            num=0    
    return s+num 

string=input("Enter a String: ")
print("Sum of all digits is: ",calculateSum(string))            
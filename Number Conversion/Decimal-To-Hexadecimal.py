num=int(input("Enter Decimal number: "))
s,i=0,0
hex=[]
while num>0:
    rem=num%16
    if rem<10:
        hex.append(rem+48)
    else:
        hex.append(rem+55)   
    num=num//16
   
hex.reverse()

print("The Hexadecimal Number is: ")
for i in hex:
    print(i,end="")  



#this program is incorrect    
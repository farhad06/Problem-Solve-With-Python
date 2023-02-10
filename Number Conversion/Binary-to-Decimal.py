num=int(input("Enter Binary number: "))
s,k=0,0
while num>0:
    rem=num%10
    s=s+rem*(2**k)
    num=num//10
    k+=1


print("The Decimal Number is: ",s)    
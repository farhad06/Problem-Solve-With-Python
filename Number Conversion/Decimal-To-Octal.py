number=int(input("Enter a Decimal Number: "))
arr=[]
while number>0:
    rem=number%8
    arr.append(rem)
    number=number//8
arr.reverse()
print("Octal number is: ")
for i in arr :
    print(i,end="")
number=int(input("Enter a Decimal Number: "))
arr=[]
while number>0:
    rem=number%2
    arr.append(rem)
    number=number//2
arr.reverse()
print("Binary number is: ")
for i in arr :
    print(i,end=" ")
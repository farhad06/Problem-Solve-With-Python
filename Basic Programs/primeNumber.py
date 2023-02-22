n=int(input("Enter a number : "))
flag=False
for i in range(2,n):
    if n % 2 ==0:
        flag=True
        break
if flag == True:
    print("The number not is prime")
else:
    print("The number is  prime")            
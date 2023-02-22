import math
n=input("Enter the range of N: ")
n=int(n)
s=0
for i in range(1,n+1):
    if i % 2==0:
        s=s+i*i
    else:
        s=s+math.factorial(i)
print("Sum of the series is: ", s)            
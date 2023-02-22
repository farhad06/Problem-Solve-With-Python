#sum of the factorial series
import math
n=input("Enter the value of n\n ")
n=int(n)
s=0
for i in range(1,n+1):
    for j in range(i,i+1):
        k=math.factorial(i)
    s=s+k 
print("The sum of the series is: ",s)       
#krishnamurthy number
import math
n=int(input("Enter a number: "))
s=0
q=n

while q > 0:
    r=q%10
    s=s+math.factorial(r)
    q=q//10

if (s==n):
    print("Inputed number is a Krishnamurty number ")
else:
    print("Inputed number is a not Krishnamurty number ") 
#krishnamurty number interval
import math
lower=int(input("Enter the lower range: "))
upper=int(input("Enter the upper range: "))

print("Krishnamurty numbers between" , lower, "and" ,upper , "are:")

for number in range(lower,upper+1):
    s=0
    q=number

    while q > 0:
        r=q%10
        s=s+math.factorial(r)
        q=q//10

    if number == s:
        print(number)    

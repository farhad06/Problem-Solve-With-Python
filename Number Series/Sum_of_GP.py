def sumOfGP(a,r,n):
    s=0 
    for i in range(n):
        s=s+a
        a=a*r 
    return s 

n=int(input("Enter number of terms(n): "))
r=int(input("Enter the common difference(r): "))
a=int(input("Enter the first terms of series(a): "))
print("Sum of GP series is: %.5f" %sumOfGP(a,r,n))

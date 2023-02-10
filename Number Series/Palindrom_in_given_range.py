def isPrime(n):
    s=0 
    while n:
        r=n%10
        s=s*10+r
        n//=10
    return s 
low=int(input("Enter the Lower Range: "))
upper=int(input("Enter the Upper Range: "))

print("The All prime numbers between "+str(low)+" and "+str(upper)+" are: ")

for i in range(low,upper+1):
    if i == isPrime(i):
        print(i,end=" ")

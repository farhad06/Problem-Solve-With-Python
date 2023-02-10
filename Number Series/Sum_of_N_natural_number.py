def sumOfNaturalNumber(n):
    s=0 
    for i in range(1,n+1):
        s=s+i 
    return s 

rng=int(input("Enter the Range: ")) 

print("The sum of first",rng,"number is: ",sumOfNaturalNumber(rng))

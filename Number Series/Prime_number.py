from math import sqrt
def isPrime(num):
    if num <=1:
        return False 
    for i in range(2,int(sqrt(num))+1):
        if num % i==0:
            return False
    return True        

n=int(input("Enter a number: "))

if isPrime(n)==True:
    print("Number is Prime")
else:
    print("Numer is not Prime")    
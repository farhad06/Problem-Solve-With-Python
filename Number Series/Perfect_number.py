def isPerfect(n):
    s=0 
    while n:
        rem=n%10
        s=s+rem
        n//=10
    return s 

number=int(input("Enter a number: "))

if isPerfect(number)==number:
    print("This is a perfect number")
else:
    print("This is a not perfect number")    
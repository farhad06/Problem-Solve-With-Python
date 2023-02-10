"""Strong Numbers are the numbers whose sum of factorial of digits is equal to the original number. Given a number, check if it is a Strong Number or not"""

def fact(n):
    f=1 
    for i in range(1,n+1):
        f*=i 
    return f 

 
def isStrong(n):
    s=0
    while n:
        r=n%10
        s=s+fact(r)
        n//=10
    return s    

number=int(input("Enter a number: ")) 
if isStrong(number)==number:
    print("Number is a Strong Number. ")
else:
    print("Number is not a Strong Number. ")                   
"""An integer number in base 10 which is divisible by the sum of its digits is said to be a Harshad Number. An n-Harshad number is an integer number divisible by the sum of its digit in base n."""
def isHarshad(num):
    s=0 
    while num:
        rem=num%10
        s=s+rem
        num=num//10

    return s   

n=int(input("Enter a number: " )) 
if n % isHarshad(n)==0:
    print("This number is Harshad number. ")
else:
    print("This is not a Harshed number. ")    

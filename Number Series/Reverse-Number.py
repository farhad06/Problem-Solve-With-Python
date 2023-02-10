def reverseNumber(num):
    s=0
    while num:
        rem=num%10
        s=s*10+rem 
        num//=10
    return s 

number=int(input("Enter a number: "))  

print("Reversed number is: ",reverseNumber(number))
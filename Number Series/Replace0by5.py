def reverseNumber(num):
    s=0
    while num:
        rem=num%10
        s=s*10+rem 
        num//=10
    return s    
def replace0by5(num):
    if num==0:
        return 5
        
    else:
        temp=0 
        while num>0:
            digit=num%10
            if digit==0:
                digit=5
            temp=temp*10+digit
            num//=10

        return  reverseNumber(temp)                

number=int(input("Enter a number: "))
print(replace0by5(number))        
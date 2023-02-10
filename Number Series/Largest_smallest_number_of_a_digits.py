def largeSmall(n):
    if len(str(n))==1:
        small=n
        maxi=n 
    else:
        maxi=0
        small=0
        while n:
            rem=n%10
            if rem >maxi:
                maxi=rem
            else:
                small=rem     
            n//=10

    return maxi,small 
n=int(input("Enter a number: "))
maxi,small=largeSmall(n)
print("The maximum digit is: ",maxi)
print("The minimum digit is: ",small)
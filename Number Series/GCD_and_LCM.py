def GCD(a,b):
    if a>b:
        small=b
    else:
        small=a 

    for i in range(1,small+1):
        if a%i==0 and b%i==0:
            gcd=i 

    return gcd 


def LCM(a,b):
    if a>b:
        greatest=a
    else:
        greatest=b 

    
    while True:
        if greatest%a==0 and greatest%b==0:
            lcm=greatest
            break
        greatest +=1     

    return lcm


num1=int(input("Enter 1st Number: "))
num2=int(input("Enter 2nd Number: "))

print("-----------------------------")

print("GCD of " +str(num1)+" and "+str(num2)+" is: "+str(GCD(num1,num2)))
print("LCM of " +str(num1)+" and "+str(num2)+" is: "+str(LCM(num1,num2)))
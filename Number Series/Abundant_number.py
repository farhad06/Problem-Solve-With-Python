"""A number n is said to be an Abundant Number if the sum of all the proper divisors of the number denoted by sum(n) is greater than the value of the number n. And the difference between these two values is called abundance."""
def isAbundant(num):
    i=1 
    s=0
    while i<num:
        if num % i==0:
            s=s+i 
        i+=1
    return s 

number=int(input("Enter a number: "))

if (isAbundant(number)-number) > 0:
    print("Yes!It is a abundant number.")
else:
    print("No!It is  not a abundant number.")    
            
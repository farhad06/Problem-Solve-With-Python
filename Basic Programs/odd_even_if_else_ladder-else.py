n=input("Enter a number: ")
n=int(n)
if n>0:
    if (n % 2) == 0:
        print("Number is positive even")
    else:
        print("Number is positive odd")
elif n<0:
    if (n % 2) == 0:
        print("Number is negative even")
    else:
        print("Number is negative odd")
else:
    print("Number is positive even")                
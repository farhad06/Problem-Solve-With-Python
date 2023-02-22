#armstrong number in an interval
lower=int(input("Enter the lower range: "))
upper=int(input("Enter the upper range: "))

print("Armstrong numbers between" , lower, "and" ,upper , "are:")

for num in range(lower,upper+1):
    no_of_digits=len(str(num))
    s=0
    q=num
    while q > 0:
        r=q%10
        s=s+ r ** no_of_digits
        q=q//10

    if num == s:
        print(num)

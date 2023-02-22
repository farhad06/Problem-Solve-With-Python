#sum of a digits of a number
n = input("Enter a number\n ")
n=int(n)
q=n
s=0
while q > 0:
    r = q % 10
    s=s+ r
    q=q//10

print("The sum is :",s)

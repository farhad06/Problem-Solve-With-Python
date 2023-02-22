#check armstrong number
n=int(input("Enter a number: "))

no_of_digits=len(str(n))
s=0
q=n

while q > 0:
    r=q%10
    s=s+ r ** no_of_digits
    q=q//10

if (s==n):
    print("Inputed number is a Armstrong number ")
else:
    print("Inputed number is a not Armstrong number ")        
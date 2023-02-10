Nth_terms=int(input("How many terms?: "))
a,b=0,1 
if Nth_terms==0:
    print("Please enter a positive terms(other than zero). ")
else:
    print("Fibonaci series is: ",end="")
    for i in range(Nth_terms):
        print(a,end=" ")
        sum=a+b
        a=b 
        b=sum 

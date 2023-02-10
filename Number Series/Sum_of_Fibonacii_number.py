def fibonaci(n):
    if n<=1:
        return n
    return fibonaci(n-1)+fibonaci(n-2)

N=int(input("Enter the Nth Term.")) 
print("Sum of Fibonaci series is: ",fibonaci(N))   


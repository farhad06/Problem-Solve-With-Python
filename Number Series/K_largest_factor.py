def KLargestNumber(n,k):
    for i in range(n,0,-1):
        if n % i==0:
            k=k-1
        if k==0:
            return i  
    return -1 

n=int(input("Enter a number: "))
k=int(input("Enter the Kth element You Want? "))
print("The Kth number is: ",KLargestNumber(n,k))

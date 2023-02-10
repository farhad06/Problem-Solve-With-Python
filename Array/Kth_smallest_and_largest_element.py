def KthSmallestNumber(arr,n,k):
    if k >n or k<=0:
        return 0
    else:    
        arr.sort()
        return arr[k-1]
def KthLargestNumber(arr,n,k):
    if k >n or k<=0:
        return 0
    else:    
        arr.sort()
        return arr[n-k]


arr = [12, 3, 5, 7, 19] 
n=len(arr)
k=int(input("Enter K value:"))

ele=KthSmallestNumber(arr,n,k)
if ele==0:
    print("K is less than the length of array and greater than zero.")
else:    
    print(f"The {k}th smallest element is:{ele}")

ele1=KthLargestNumber(arr,n,k)
if ele1==0:
    print("K is less than the length of array and greater than zero.")
else:    
    print(f"The {k}th largest element is:{ele1}")

def missingNumber(arr):
    n=len(arr)
    total=((n+1)*(n+2))//2 
    s=0 
    for i in arr:
        s+=i 
    return total-s 

arr = [1, 2, 3, 5,4,7]
# arr=[3,0,1]
print("Missing Number is:",missingNumber(arr))        
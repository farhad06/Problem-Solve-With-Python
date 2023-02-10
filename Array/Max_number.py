def maxNumber(arr):
    max=arr[0]
    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i] 
    return max 

arr=[2,3,4,10,34,0,7]
print("Maximum number in this array is: ",maxNumber(arr))
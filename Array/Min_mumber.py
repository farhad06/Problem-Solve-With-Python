def minNumber(arr):
    min=arr[0]
    for i in range(len(arr)):
        if arr[i]<min:
            min=arr[i] 
    return min

arr=[2,3,4,10,34,78,7]
print("Minimum number in this array is: ",minNumber(arr))
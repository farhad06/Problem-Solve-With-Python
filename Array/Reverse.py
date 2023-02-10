def reverse(arr):
    low=0
    high=len(arr)-1
    while low<high:
        temp=arr[low]
        arr[low]=arr[high]
        arr[high]=temp
        low+=1
        high-=1
    return arr 
arr = [12, 13, 1, 10, 34, 1]  
print("Reverse array is: ",reverse(arr))


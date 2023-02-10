def moveNegative(arr):
    n=len(arr)
    j=0
    for i in range(n):
        if arr[i]<0:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            j+=1

    return arr 

arr=[-12,11,-13,-5,6,-7,5,-3,-6]
print("New array is:",moveNegative(arr))            
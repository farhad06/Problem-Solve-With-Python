def rotate(arr,n):
    # x=arr[n:=len(arr)-1]
    x=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]

    arr[0]=x 

    # return arr 

arr=[1,2,3,4,5]
n=len(arr)
rotate(arr,n)
print("After rotate the array is:")
for i in arr:
    print(i,end=" ")

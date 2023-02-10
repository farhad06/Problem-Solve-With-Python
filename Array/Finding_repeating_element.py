def repeateElement(arr):
    n=len(arr)
    ele=[]

    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                ele.append(arr[i])
    return ele 

# arr=[1,1,2,3,4,4,5,2]
arr=[1,1,0]
print("Duplicate elements are: ",repeateElement(arr))
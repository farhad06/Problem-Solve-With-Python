def leftRotation(arr,d):
    n=len(arr)
    temp=[]
    for i in range(d,n):
        temp.append(arr[i])

    for i in range(d):
        temp.append(arr[i]) 

    # for i in range(n):
    #     arr.append(temp[i])

    return temp   

arr=[3, 4, 5, 6, 7, 1, 2]  
d=3 
print(leftRotation(arr,d))              
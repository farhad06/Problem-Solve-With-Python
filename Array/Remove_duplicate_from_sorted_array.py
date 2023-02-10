def removeDuplicate(arr):
    count=0 
    n=len(arr)
    for i in range(1,n):
        if arr[count]!=arr[i]:
            count+=1
            arr[count]=arr[i]
    return count+1        
    

arr=[1,1,2,2,2,3,3]
k=removeDuplicate(arr)
print("New array is: ")
for i in range(k):
    print(arr[i],end=" ")                
def frequencyCount(arr,n):
    visited=[False for i in range(n)]
    for i in range(n):
        if visited[i] == True:
            continue 
        count=1
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                visited[j]=True
                count+=1 
        print(arr[i],count)        
             
arr = [10, 20, 20, 10, 10, 20, 5, 20]
n = len(arr)
frequencyCount(arr,n)
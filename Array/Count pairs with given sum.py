def countPair(arr,sum):
    count=0
    n=len(arr) 
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==sum:
                count+=1 
    return count 

arr=[10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1] 
s=int(input("Enter sum: "))
print("Number of sum count Pair is:",countPair(arr,s))               

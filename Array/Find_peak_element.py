def findPeak(arr):
    n=len(arr)

    #check for 1st or last element as a peak element 
    if n==1:
        return arr[0] 
    if arr[0]>=arr[1]:
        return arr[0] 
    if arr[n-1]>=arr[n-2]:
        return arr[n-1] 
    #check for other element 
    for i in range(1,n-1):
        if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
            return arr[i] 
# arr = [ 1, 3, 20, 4, 1, 0 ]
#arr=[1,2,34,50,60]
#arr=[20]
arr=[10, 20, 15, 2, 23, 90, 67]

print("Peak Element is:",findPeak(arr))                   
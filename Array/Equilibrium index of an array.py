def equilibrium(arr):
    n=len(arr)
    for i in range(n):
        left_sum=0
        right_sum=0
        for j in range(i):
            left_sum+=arr[j] 
        for j in range(i+1,n):
            right_sum+=arr[j]

        if left_sum==right_sum:
            return i 

    return -1 

# arr = [-7, 1, 5, 2, -4, 3, 0]  
arr=[1,2,3]

print(equilibrium(arr))



def iszero(arr):
    n=len(arr)
    sub_arr=[[]]
    for i in range(n+1):
        for j in range(i):
            sub_arr.append(arr[j:i])

    for i in range(len(sub_arr)):
        if len(sub_arr[i])>0 and sum(sub_arr[i])==0:
            return True
    return False 

# arr=[-3, 2, 3, 1, 6]
arr=[4, 2, 0, 1, 6] 

if iszero(arr):
    print("There is a sub array where sum equal to zero.")
else:
     print("There is no sub array where sum equal to zero.")    

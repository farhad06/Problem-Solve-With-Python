def create(arr):
    n=len(arr)
    sub_arr=[[]]
    for i in range(n+1):
        for j in range(i):
            sub_arr.append(arr[j:i])

    return sub_arr        

arr=[1,2,3,4]
print("Sub arrays are:",create(arr))  
# sub_arr=create(arr)
# print(sum(sub_arr[4]))           
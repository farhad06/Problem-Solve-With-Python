def K_right_rotate(arr,k):
    n=len(arr)
    k=k%n # if rotation is greater than size of array. 
    for i in range(n):
      if i<k:
        print(arr[n+i-k],end=" ")
      else:
        print(arr[i-k],end=" ") 
    # print("\n")     

arr=[1,2,3,4,5]
k=2 
print(K_right_rotate(arr,k))            

    
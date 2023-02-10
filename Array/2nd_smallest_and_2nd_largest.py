def secondLargest(arr):
    large=arr[0]
    for i in arr:
        if i>large:
            large=i
    Second_large=arr[0] 
    for i in arr: 
        if i > Second_large and i<large:
            Second_large=i 
    return large,Second_large


def secondSmall(arr):
    small=arr[0]
    for i in arr:
        if i <small:
            small=i
    second_small=arr[0]
    for i in arr:
        if i<second_small and i >small:
            second_small=i      

    return small ,second_small


arr = [12, 13, 1, 10, 34, 1]    
large,large_2nd=secondLargest(arr)
print("Large Element is: "+str(large)+" and "+" Second Large element is: " +str(large_2nd))

small,small_2nd=secondSmall(arr)
print("Small Element is: "+str(small)+" and "+" Second Small element is: " +str(small_2nd))


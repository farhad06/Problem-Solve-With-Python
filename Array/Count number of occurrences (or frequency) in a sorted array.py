def count(arr,ele):
    count=0
    for i in arr:
        if i==ele:
            count+=1
    return count


arr=[1, 1, 2, 2, 2, 2, 3]
ele=int(input("Enter the element."))
print("Number of occurance is:",count(arr,ele))           
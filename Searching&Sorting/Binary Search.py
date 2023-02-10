                                        ######## Binary Search ######

def binarySearch(l,size,start,end,key):
    while start<=end:
        mid=(start+end)//2
        if l[mid]==key:
            return 1 
        if key>l[mid]:
            start=mid+1
        else:
            end=mid-1
    return 0        
    
    
lst=[2,3,12,56,100,5]
lst.sort()
n=len(lst)
star=0
end=n-1
ele=5
if binarySearch(lst,n,star,end,ele)==1:
    print("Number is found")
else:
    print("Number is not found")
 
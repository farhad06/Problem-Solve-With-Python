                                        ######## Bubble Sort ######


def bubbleSort(l,size):
    for i in range(size-1):
        for j in range(size-1-i):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
                
            
    
    
lst=[2,30,12,56,100,5,1]
print("Before Sort the array is: \n",lst)
bubbleSort(lst,len(lst))
print("After Sort the array is: \n",lst)

 
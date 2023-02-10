                                        ######## Selection Sort ######

def selectionSort(l,size):
    for i in range(size-1):
        for j in range(i+1,size):
            if l[i]>l[j]:
                temp=l[i]
                l[i]=l[j]
                l[j]=temp
                
            
    
    
lst=[2,30,12,56,100,5,1]
print("Before Sort the array is: \n",lst)
selectionSort(lst,len(lst))
print("After Sort the array is: \n",lst)

 
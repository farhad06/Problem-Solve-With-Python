                                    ############### Linear Search ################## 
List=[6,2,8,10,1,20]
serach=123 

def linearSearch(l,size,s):
    for i in range(size):
        if l[i]==s:
            return 1 
    return 0 

N=len(List)

if linearSearch(List,N,serach)==1:
    print("Number is found")
else:
    print("Number is not found")

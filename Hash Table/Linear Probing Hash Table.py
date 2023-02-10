                        ########## Linear Probing Hash Table #############
import sys
#create a list whose all elements are -1
def init():
    arr=[-1 for i in range(5)]
    return arr

#insert value into the hash table
def insertValue(arr):
    val=int(input("Enter a number of element: "))
    size=len(arr)
    key=val%size
    index=key
    
    while arr[index]!=-1:
        index=(index+1)%size
        if index==key:
            print("Hash Table Full")
            return 0
    arr[index]=val
    return 1 
#display the hash table     
def display(arr):
    # size=len(arr)
    for i in arr:
        print(i)

#delete elements from hash tabel 
def deleteElements(arr):
    val=int(input("Enter the element to be deleted: "))
    size=len(arr)
    key=val%size
    index=key
    
    while arr[index]!=val:
        index=(index+1)%size
        if index==key:
            # print("Hash Table Full")
            return 0
    arr[index]=-1
    return 1 
#search a value in hash Table
def searchValue(arr):
    val=int(input("Enter the element to be search: "))
    size=len(arr)
    key=val%size
    index=key
    
    while arr[index]!=val:
        index=(index+1)%size
        if index==key:
            return 0
    return 1 
       
    
arr=init()
while True:
    print("1.Insert || 2.Display || 3. Exit || 4.Delete || 5.Search ")
    ch=input("Enter Your Choice: ")
    if ch=='1':
        insertValue(arr)
    elif ch=='2':
        display(arr)
    elif ch=='4':
        deleteElements(arr)
    elif ch=='3':
        sys.exit("You Exit the program. ")
    elif ch=='5':
        if (searchValue(arr)==1):
            print("Element Found in the Hash Table")
        else:
            print("Element Not Found in the Hash Table")
    else:
        print("Wrong Choice. ")
        

    



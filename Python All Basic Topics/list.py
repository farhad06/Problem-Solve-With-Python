'''List is a python datatype which is used to store multiple variable in a single variable
List is ordered,changeable and allow duplicate value
'''
#create & print a list
l=[1,2,3,4,5]
print(l)
li=list(("Farhad",1,2.2,True))
print(li)
#insert a value in aspacific position in the list
li.insert(3,"Apple")
print(li)
##add the element at the end of the list
thislist=[1,2,3,4,2.24,5.6,True,"Rohit",False,"apple",[7,8,9]]
print(thislist)
thislist.append("banana")
print(thislist)
#remove all the element from the list
l1=[1,2,3,45,6,7]
print(l1)
l1.clear()
print(l1)
##copy list
copy_thislist=thislist.copy()
print(copy_thislist)
##count an element in the list
cnt=copy_thislist.count(3)
print(cnt)
#position of a value in the list
print(thislist.index(2.24))
#remove  a element from a list
thislist.pop(5)
print(thislist)
thislist.remove(False)
print(thislist)
#reverse the list
L=[1,2,3,4,5,6,7,8,9,10]
print(L)
L.reverse()
print(L)
#sort list
L1=[1,5,2,8,45,6,0,10,87,125,3,6]
print(L1)
L1.sort()
print(L1)
#join two list
l2=[1,2,3,4,5]
l3=[6,7,8,9,10]
l4=l2+l3
print(l4)
for i in l3:
    l2.append(i)
print(l2)
l2.extend(l3)
print(l2)
'''Thera are two types of loop
1.for loop
2.while loop
'''
#for
l=[1,2,3,4,5]
sum=0
for i in l:
    sum=sum+i
print("The sum is: ",sum)
#for with else
print("*****************************************************")
digits=[0,1,5]
for i in digits:
    print(i)
else:
    print("No items are left in this list")
print("*****************************************************")
##while
n=10
i=1
sum=10
while i<=n:
    sum=sum+i
    i+=1
print("Sum is: ",sum)
print("*****************************************************")
#while with else
counter=0
while counter<3:
    print("Inside loop")
    counter+=1
else:
    print("Inside else")

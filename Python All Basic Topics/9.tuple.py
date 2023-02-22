'''Tuple is used to store multiple element in a single variable
Tuple is ordered and unchangable
'''
#create a print a tuple
tup=(1,2,3,"apple",True,2.6)
print(tup)
tup1=tuple((1,2,3,7,88,99))
print(tup1)
#change and update element
x=(1,2,3,4)
y=list(x)
y[2]=2.6
x=tuple(y)
print(x)
thistup=("apple","banana","mango",1)
thistup1=("pineapple",)
thistup+=thistup1
print(thistup)
#unpack tuple
(a,b,c,d,e)=thistup
print("Unpacking the tuple elements")
print(a);print(b);print(c);print(d);print(e)
'''All the function are same as list method'''
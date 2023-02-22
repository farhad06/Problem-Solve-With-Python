'''List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.'''
#syntax:---> newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
print("The upper program execute using list comprehension")
newlist1=[x for x in fruits if "a" in x]
print(newlist1)
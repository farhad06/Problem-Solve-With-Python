#zip() function
'''The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.'''
a=[1,2,3,4,5,6,7]
b=[10,202,20,23,25,45]
x=zip(a,b)
print(dict(x))


#map() function
'''map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)'''
''' Syntax  map(fun,iter)'''

def addition(a):
    return a+a
l=(1,2,3,4,5)
result=map(addition,l)
print(list(result))
#filter
'''The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.'''
# function that filters vowels
def fun(variable):
	letters = ['a', 'e', 'i', 'o', 'u']
	if (variable in letters):
		return True
	else:
		return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
	print(s)

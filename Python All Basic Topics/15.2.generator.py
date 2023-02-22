''' A generator is a spacial type of function which dows not return a single value ,instead ,it returns
it returns an iterator object which a sequence  of values.In a generator a yield statement is used rather than
a return statement.
'''
def mygenerator():
    print('First item')
    yield 10
    print('Second item')
    yield 20
    print('Last item')
    yield 30

gen = mygenerator()
next(gen)
next(gen)
next(gen)
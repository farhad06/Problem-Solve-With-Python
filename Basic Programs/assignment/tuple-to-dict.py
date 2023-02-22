# Python code to convert into dictionary
def tupleToDict(tup, di):
	di = dict(tup)
	return di
	
tups = [("Rohit", 45), ("Virat", 18), ("Dhoni", 7),
	("Hardik", 33), ("Bumrah", 99)]
dictionary = {}
print (tupleToDict(tups, dictionary))

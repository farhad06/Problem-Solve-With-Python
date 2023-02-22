'''Dictionary is a python datatype which is store value in key value pair
Dictionary is----
1.Ordered
2.Changeable
3.Do not allow duplicate
'''
#create and print
thisdict={
    "roll":45,
    "name":"Rohit",
    "home":"nagpur",
    "year":1980
}
print(thisdict)
##access the item in this dict
x=thisdict["roll"]
x1=thisdict.get("name")
print(x);print(x1)
#get all the keys in this dict
keys=thisdict.keys()
print(keys)
thisdict["team"]="India"
print(keys)
#get all the values in this dict
val=thisdict.values()
print(val)
#get key value pair
item=thisdict.items()
print(item)
#change item
thisdict['home']="Mumbai"
print(thisdict)
thisdict.update({"highest":264})
print(thisdict)
#loop in this dictionary
for i in thisdict:
    print(i) #only get keys
print("The keys are: ")
for key in thisdict.keys():
    print(key)
print("The values are: ")
for val in thisdict.values():
    print(key)
print("The items are: ")
for key,val in thisdict.items():
    print(key,"=>",val)
###copy dict
thisdict1=thisdict.copy()
print(thisdict1)
thisdict2=dict(thisdict)
print(thisdict2)
##nested dict
indiateam={
    "pl1":{
        "name":"Rohit",
        "Jersy no":45
    },
    "pl2": {
    "name": "Virat",
    "Jersy no": 18
    },
    "pl3": {
        "name": "Pant",
        "Jersy no": 77
        }
}
print(indiateam)

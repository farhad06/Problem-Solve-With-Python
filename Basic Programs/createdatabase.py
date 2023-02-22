import pymongo
from pymongo import MongoClient
client=MongoClient('localhost',27017)
#use('user')
db=client['school']
collection=db['pla']
'''print("Database created\n")
print("List of databses are")
print(client.list_database_names())'''
#print("collection created")
''''doc1={"name":"Rashid Khan","age":24,"home":"Afganistan","franchise":"Sunrise Hydrabad"}
doc2={"name":"Hardik","age":28,"home":"Gujrat","franchise":"Mumbai Indians"}
doc3={"name":"KL Rahul","age":27,"home":"Karnataka","franchise":"Punjab Kings"}
doc4={"name":"Jadeja","age":32,"home":"Gujrat","franchise":"Chennai Super Kings"}
doc5={"name":"Gill","age":23,"home":"Punjab","franchise":"Kolkata Kinht Riders"}
doc6={"name":"Pant","age":22,"home":"Delhi","franchise":"Delhi Capitals"}
#collection.insert_many([doc1,doc2,doc3,doc4,doc5,doc6])
for i in collection.find().sort("name",-1):
    print(i)'''
qu={"name":"Rashid Khan"}
#newvalue={"$set":{"home":"Nagpur"}}
collection.delete_one(qu)
for x in collection.find(qu):
    print (x)
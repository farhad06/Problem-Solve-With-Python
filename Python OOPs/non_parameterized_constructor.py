class Person:
    def __init__(self):
        print("This is a non parameterized constructor")
    def bio(self,name):
        #name=self.name
        print("This person name is: ",name)
obj=Person()
obj.bio("Virat")
#print(obj.__dir__)
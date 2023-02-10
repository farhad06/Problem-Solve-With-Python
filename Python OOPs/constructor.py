class Person:
    def __init__(self, name, roll):
        self.name=name
        self.roll=roll
    def disp (self):
        name=self.name
        roll=self.roll
        print("Name is:" , name)
        print("Roll is:" , roll)
obj1=Person("Manoj" , 102)
obj1.disp()
print()
obj2=Person("Rohit" , 45)
obj2.disp()
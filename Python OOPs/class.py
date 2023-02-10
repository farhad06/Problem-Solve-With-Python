class Student:
    roll=20
    name="Manoj Pal"
    def bio(self):
        roll=self.roll
        name=self.name
        print("Name of the Student is: ",name," and Roll number is: ",roll)
obj=Student()
#del obj.roll
obj.bio()
del obj
#obj.bio()
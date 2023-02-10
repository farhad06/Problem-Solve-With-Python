'''All variable which are assigned a value in class declaration are class variable and variable which are
assigned values inside the methods are instance variable'''
class Student:
    stream="CSE" #class variable
    def __init__(self,name,roll):
        self.name=name #Instance variable
        self.roll=roll
a=Student("Rohit",45)
b=Student("Virat",18)
for stu in(a,b):
    print("*****************************************")
    print(stu.stream)
    print(stu.name)
    print(stu.roll)
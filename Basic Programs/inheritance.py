#base class
class Person():
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    def isEmployee(self):
        return False
#derived class
class Employee(Person):
    def isEmployee(self):
        return True
#using super 
    #super(Employee, self).__init__(x)

emp=Person("Greek1")
print(emp.getName(),emp.isEmployee())
emp=Employee("Greek2")
print(emp.getName(),emp.isEmployee())                        
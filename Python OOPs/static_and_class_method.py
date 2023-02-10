#Class method
'''
1.A class method is a method which is bound to the class and not the object of the class
2.They have the access to the state of the class as it takes a class parameter that points
to the class and not the object instance
3.It can modify a class state that would apply across all the instance of the class. For example
it can modify a class variable that will be applicable to all the instance
'''
#Static method
'''
1.A static method is also a method which is bound to the class and not the object of the class.
2.A static method can not access or modify class state.
3.It present in a class because it makes sense for the method to be present in class
'''

from datetime import date as dt
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #static method
    def isAdult(age):
        if age>18:
            return True
        else:
            return False
    #class method
    def emp_from_year(emp_class,name,year):
        return emp_class(name,dt.today().year - year)
    def __str__(self):
        return 'Employee Name: {} and Age: {}'.format(self.name,self.age)
e1=Employee('Dhiman',25)
print(e1)
e2=Employee.emp_from_year('Subhas',1987)
print(e2)
print(Employee.isAdult(25))
print(Employee.isAdult(16))
###Public Access Modifiers
print("Public Access Modifiers")
class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def disp(self):
        print("Roll",self.roll)
obj=Student("Ravi Kumar",3)
print("Name:" ,obj.name)
obj.disp()
print("*********************************************************************************************")
print("Protected Access Modifiers")
class Student1:
    _name=None
    _roll=None
    _stream=None
    def __init__(self,name,roll,stream):
        self._name=name
        self._roll=roll
        self._stream=stream
    def _disp(self):
        print("Roll is: ",self._roll)
        print("Stream is ",self._stream)
class School(Student1):
    def __init__(self,name,roll,stream):
        Student1.__init__(self,name,roll,stream)
    def dispDetails(self):
        print("Name is: ",self._name)
        self._disp()
new_obj=School("Ramesh",25,"BTech")
new_obj.dispDetails()
print("***************************************************************************************")
print("Private access specifiers")
class College:
    __name=None
    __roll=None
    __branch=None
    def __init__(self,name,roll,branch):
        self.__name=name
        self.__roll=roll
        self.__branch=branch
    def __disp(self):
        print("Name is: ",self.__name)
        print("Roll is: ",self.__roll)
        print("Branch is: ",self.__branch)
    def dispDetails(self):
        self.__disp()
obj1=College("Rakesh",45,"MCA")
obj1.dispDetails()
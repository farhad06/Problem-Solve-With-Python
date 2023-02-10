'''
############################# PYTHON ALL OPPS CONCEPTS ##############################
##Simple Class
class Stu:
    name="Rahul"
    roll=20
    
    def bio(self):
        name=self.name
        roll=self.roll
    def print(self):
        print("Name is: ",self.name,"Roll is ",self.roll)

obj=Stu()
obj.print()

###Class with constructor
class con:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def dis(self):
        print("Name is==>",self.name,"Roll is===>",self.roll)
obj=con('Rohit',45)
obj.dis()
print()
obj=con('Virat',18)
obj.dis()

###Single Inheritance
class Player:
    def bat(self):
        print("They Can Bat")
class Bowl(Player):
    def bowl(self):
        print("They also can Bowl well")
all_rounders=Bowl()      
all_rounders.bat()
all_rounders.bowl()

###Multilevel Inheritance
class Base:
    def base_class(self):
        print("This is Base class")
        
class Intermidiate(Base):
    def intermideate_class(self):
         print("Hi! I am Intermideate Class")
class Child(Intermidiate):
    def child_class(self):
        print("I am Child class 😇")
obj=Child()

obj.base_class()
obj.intermideate_class()
obj.child_class()

##Multiple Inheritance
class Father:
    def father(self):
        print("I am Father 🧞️")
class Mother:
    def mother(self):
        print("I am Mother 🧞️")
class Brother:
    def brother(self):
        print("I am Brother 😊")
class Sister:
    def sister(self):
        print("I am Sister 😗")
class Family(Father,Mother,Brother,Sister):
    def family(self):
        print("We are Family 👨👨👦👦")
obj=Family()
obj.father()
obj.mother()
obj.brother()
obj.sister()
print()
obj.family()

####Ploymorphisms

class A:
    def _print(self):
        print("This is A")
class B:
    def _print(self):
        print("This is B")
class C:
    def _print(self):
        print("This is C")
        
obj_A=A()  
obj_B=B()        
obj_C=C()

for obj in (obj_A,obj_B,obj_C):
    obj._print()



####Method Overrriden
class overrriden:
    def overriden_(self):
        print("Hi I am Define in Base Class")
    def fun(self):
        print("This is a normal function")
class derived_1(overrriden):
    def fun(self):
        print("This is a normal function in Derived-1 class")
class derived_2(overrriden):
    def fun(self):
        print("This is a normal function in Derived-2 class") 
obj_overriden=overrriden()
obj_derived_1=derived_1()
obj_derived_2=derived_2()

for obj in (obj_overriden,obj_derived_1,obj_derived_2):
    print()
    obj.overriden_()
    obj.fun()

############################## END ########################################    
    
'''''''    

        
        


         

        
        
        

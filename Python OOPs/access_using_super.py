class Base:
    #__hiddenvar=100
    def __init__(self,a):
        self.a=a
class Derived(Base):
    def __init__(self,a,b):
        super(Derived, self).__init__(a)
        self.b=b
    def print(self):
        print(self.a,self.b)
d=Derived(10,20)
#base=Base()
d.print()
#print(base._Base.__hiddenvar)
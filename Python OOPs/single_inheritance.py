class Player:# base class
    def bat(self):
        print("He can Bat very well")
class Bowl(Player): # child class
    def bowl(self):
        print("He can also bowl")
hardik=Bowl() #create object for base class
hardik.bat() #access the base class function
hardik.bowl() #access the child class function
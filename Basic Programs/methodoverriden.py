class Bird:
    def intro(self):
        print("There are many types of birds")
    def flight(self):
        print("Most of the bird can fly but some cannot")
class sparrow(Bird):
    def flight(self):
        print("Sparrow can fly")
class ostrich(Bird):
    def flight(self):
        print("Ostrich can not fly")   

bird=Bird()
spr=sparrow()
ost=ostrich()

bird.intro()
bird.flight()
print("------------------------------------------------------------")
spr.intro()
spr.flight()
print("------------------------------------------------------------")
ost.intro()
ost.flight()
#print("------------------------------------------------------------")
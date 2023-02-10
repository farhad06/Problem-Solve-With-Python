class Road:
    def bus(self):
        print("Bus ,Train,Taxi are the Road Transportation")
class River(Road):
    def boat(self):
        print("Boat, Steamer are the River Transportation")
class Sky(River):
    def plane(self):
        print("Plane is the Sky Transportation")
transportation=Sky()
transportation.bus()
transportation.boat()
transportation.plane()



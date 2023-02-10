class Player:
    def intro(self):
        print("There are 11 players in a team")
    def role(self):
        print("Some players can Only Bat,Some players can Only Bowl and Some Players Can do Bat & Bowl Simuteniously")
class Batter(Player):
    def role(self):
        print("There are 4 batters in a team")
class Bowler(Player):
    def role(self):
        print("There are 4 blowers in a team")
class Allrounder(Player):
    def role(self):
        print("There are 3 allrounders in a team")
obj_player=Player()
obj_bat=Batter()
obj_bowl=Bowler()
obj_all=Allrounder()

for i in(obj_player,obj_bat,obj_bowl,obj_all):
    print("-----------------------------------------")
    i.intro()
    i.role()


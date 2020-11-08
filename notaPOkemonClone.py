
class player ():
    def _init_(self, name ="", health = 0, speed=0,moves={}):
        self.name = name
        self.health = health
        self.speed = speed
        self.moves = moves 
    
    def nameSet(self):
        name =""
        while name == "":
            name = input("Please enter the name for your character\n")
            check = input("Is "+ name+ " okay?\n [1] Yes     [2] No\n")
            if check == '2':
                name = ""
            elif check == '1':
                print("Your name is "+ name+".\n")
            else: 
                name = ""
                print("That is not a valid input.\n")
        self.name = name

    def getName(self):
        return self.name

    def healthSet(self,health):
        self.health = health

    def getHealth(self):
        return self.health

    def getSpd(self):
        return self.speed

    def setSpd(self,speed):
        self.speed = speed
    def MoveSelect(self,move):
        return self.moves[move] 
    def setMoves(self, moves):
        self.moves = moves


    pass
def battleSetUp():
    choice = input("[1]Player vs Player          [2]Player vs Computer")
    if choice == "1":
        choice = input("")
        player1 = playerSetUp()

def playerSetUp():
    p = player()
    p._init_()
    print("Player 1 Setup")
    p.nameSet(input("What name should your character have."))
    return p


def Choose_Moves():
    Preset_Moves = {"Hyper Beam" : 150,
    "Fire Blast" : 110,
    "Earthquake" : 100,
    "Leaf Storm" : 130,
    "Thunder Bolt" : 90,
    "Close Combat" : 120,
    "Psychic" : 90,
    "Blizzard": 110,
    "Bullet punch" : 40,
    "Tackle" : 40,
    "Hidden Power" : 60,
    "Night Slash" : 70,
    "Aerial Ace" : 60,
    "WOAH WOAH WOAH" : 200
    } 
    p = player() 
    p._init_()
    
    print(Preset_Moves)
    Chosen_Moves = list(map(str,input("Please choose 2 moves from this list").split()))
    player_chosen_moves = {}


    for x in Chosen_Moves: 
        if x in Preset_Moves:
            player_chosen_moves[x] = Preset_Moves[x]
    
    p.setMoves(player_chosen_moves)
    print(p.moves)
if __name__ == "__main__":
    Choose_Moves()
    


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
        player1 = playerSetUp("1")

def playerSetUp(number):
    p = player()
    p._init_()
    print("Player "+number +" Setup")
    p.nameSet(input("What name should your character have."))
    return p


def Choose_Moves():
    Preset_Moves = {"Hyper Beam" : 15,
    "Fire Blast" : 11,
    "Earthquake" : 10,
    "Leaf Storm" : 13,
    "Thunder Bolt" : 9,
    "Close Combat" : 12,
    "Psychic" : 9,
    "Blizzard": 11,
    "Bullet punch" : 4,
    "Tackle" : 4,
    "Hidden Power" : 6,
    "Night Slash" : 7,
    "Aerial Ace" : 6,
    } 
    p = player()
    p._init_()
    
    print(Preset_Moves)
    Chosen_Moves = []
    
    while not set(Chosen_Moves).intersection(Preset_Moves.keys()):
        Chosen_Moves.append(str(input("Please choose your first move from the moves list above (CASE SENSITIVE):   ")))
        Chosen_Moves.append(str(input("Please choose your second and last move for the moves list above (CASE SENSITIVE):   ")))
    
    player_chosen_moves = {}
    for x in Chosen_Moves: 
        if x in Preset_Moves:
            player_chosen_moves[x] = Preset_Moves[x]
    
    p.setMoves(player_chosen_moves)
if __name__ == "__main__":
    Choose_Moves()
    
def battle():

    pass

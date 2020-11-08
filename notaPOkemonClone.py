import random
class player ():
    def _init_(self, name ="", health = 50, speed=1,moves={}):
        self.name = name
        self.health = health
        self.speed = speed
        self.moves = moves 
        self.attack = 1

    def nameSet(self):
        name =""
        while name == "":
            name = input("Please enter the name for your character\n")
            check = input("Is "+ name+ " okay?\n[1] Yes     [2] No\n")
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
        return self.moves[move][0]
    def AccuracySelect(self, move):
        return self.moves[move][1] 
    def setMoves(self, moves):
        self.moves = moves
    def setAttack(self, attack):
        self.attack = attack
    def getAttack(self):
        return self.attack
    def getMoves(self):
        return self.moves
    def getMove1Name(self):
        list1 = list(self.moves.keys())
        return list1[0]
    def getMove2Name(self):
        list1 = list(self.moves.keys())
        return list1[1]
    pass
class AI(player):
    def nameManualSet(self, name):
        self.name = name
    pass
    def randomMove(self):
        list1 = list(self.moves.keys())
        return list1[random.randint(0,1)]
    

def battleSetUp():
    player = playerSetUp()
    ai = aiSetup("Francis")
    print(ai.name +" challenges you to a fight.")
    battle(player,ai,1)
    player.healthSet(50)
    ai2 = aiSetup("Ishaan")
    print(ai2.name +" challenges you to a fight.")
    battle(player,ai2,1)
    player.healthSet(50)
    ai3 = aiSetup("Reynel")
    print(ai3.name +" challenges you to a fight.")
    battle(player,ai3,1)
    player.healthSet(50)
    ai4 = aiSetup("Defrim")
    print(ai4.name +" challenges you to a fight.")
    battle(player,ai4,1)
def playerSetUp():
    p = player()
    p._init_()
    print("Player Setup")
    p.nameSet()
    moves = Choose_Moves()
    p.setMoves(moves)
    return p

def aiSetup(name):
    ai = AI()
    ai.nameManualSet(name)
    if ai.name == "Defrim":
        ai.healthSet(80)
        ai.setAttack(0.7)
        ai.setSpd(0.7)
        moves = {"WOAH WOAH WOAH": [14,.55], 
        "I'm actually done dud": [8,.75]}
        ai.setMoves(moves)
    elif ai.name == "Reynel":
        ai.healthSet(30)
        ai.setAttack(1.8)
        ai.setSpd(1.2)
        moves = {"Chancla Throw": [9,.86], 
        "Tight Hug": [7,.92]}
        ai.setMoves(moves)
    elif ai.name == "Francis":
        ai.healthSet(40)
        ai.setAttack(0.8)
        ai.setSpd(2.2)
        moves = {"Salmonela": [14,.50],
        "Monster Energy": [10,0.70]}
        ai.setMoves(moves)
    elif ai.name == "Ishaan":
        ai.healthSet(50)
        ai.setAttack(1.2)
        ai.setSpd(1.8)
        moves ={"SquadW": [4,1.00],
        "Microsoft Paint": [6,1.00]}
        ai.setMoves(moves)
    return ai


def Choose_Moves():
    Preset_Moves = {"Hyper Beam" : [15, 0.40],
    "Fire Blast" : [11,.70],
    "Earthquake" : [10 , .70],
    "Leaf Storm" : [13, .60],
    "Thunder Bolt" : [9, .80],
    "Close Combat" : [12, .60],
    "Psychic" : [9,.80],
    "Blizzard": [11,.65],
    "Bullet punch" : [4,1.00],
    "Tackle" : [4, 1.00],
    "Hidden Power" : [6,.85],
    "Night Slash" : [7,.80],
    "Aerial Ace" : [6,.85],
    }
    
    print("Moves List: Will be in the form of ===> Move Name : [Damage, Accuracy])")
    print(Preset_Moves)
    Chosen_Moves = []
    
    while not set(Chosen_Moves).intersection(Preset_Moves.keys()):
        Chosen_Moves.append(str(input("Please choose your first move from the moves list above (CASE SENSITIVE):   ")))
        Chosen_Moves.append(str(input("Please choose your second and last move for the moves list above (CASE SENSITIVE):   ")))
    
    player_chosen_moves = {}


    for x in Chosen_Moves: 
        if x in Preset_Moves:
            player_chosen_moves[x] = Preset_Moves[x]
    
    return player_chosen_moves

def battle(player, ai,turn):
    if ai.health >0 and player.health >0:
        loop = True
        while loop == True:
            health = round(player.getHealth())
            aiHealth = ai.getHealth()
            print("Turn #" + str(turn))
            print(player.getName() + " Health: "+ str(health) + "   "+ai.getName()+" Health: "+ str(aiHealth))
            choice = int(input("Which move do you want to use?\n[1] "+player.getMove1Name() + "    [2] "+player.getMove2Name() + "\n"))
            if choice == 1:
                loop = False
                attackStep(player,ai,player.getMove1Name(),turn)
            elif choice == 2:
                loop = False
                attackStep(player,ai,player.getMove2Name(),turn)
            else:
                print("1 and 2 are the only valid inputs.")

    pass
def attackStep(player,ai,move,turn):
    aimove = ai.randomMove()
    if player.getSpd() > ai.getSpd():
        ai = accCheck(player,ai,move)
        if ai.getHealth() <= 0:
            victory(player)
        else:
            player = accCheck(ai,player,move =aimove)
            if player.getHealth() <= 0:
                defeat(ai)
    else:
        player = accCheck(ai,player,move =aimove)
        if player.getHealth() <= 0:
            defeat(ai)
        else:
            ai = accCheck(player,ai,move)
            if ai.getHealth() <= 0:
                victory(player)
    turn += 1
    battle(player,ai,turn)

def damageCalc(player,move):
    damage = player.getAttack() * player.MoveSelect(move)
    return round(damage)
def accCheck(player,ai,move):
    chance = random.random()
    if chance <= player.AccuracySelect(move):
        damage = damageCalc(player,move)
        print("\n"+player.getName()+ " uses "+ move+ " and "+ ai.getName() + " takes " + str(damage) + " damage" )
        ai.healthSet(ai.getHealth() - damage)
    else: 
        print("\n"+player.getName()+ " uses "+ move+ " but it missed." )
    return ai
def victory(player):
    print(player.getName() + " wins the fight.")

def defeat(ai):
    print(ai.getName() + " wins the fight.")
    print("GAME OVER")
if __name__ == "__main__":
    battleSetUp()
    
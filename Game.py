
class player ():
    def _init_(self, name ="", health = 20):
        self.name = name
        self.health = health
        self.inventory = []
        for i in range(10):
            self.inventory.append("Empty")

    def printInv(self):
        for i in range (len(self.inventory)):
                print("Slot#"+str(i+1)+" "+ self.inventory[i])
        pass

    def itemAdd(self,item):
        for i in range(len(self.inventory)):
            if self.inventory[i] == "Empty":
                self.inventory[i] = item
                print(item +" was added to inventory.\n")
                break
            elif i == len(self.inventory)-1:
                print("Your inventory is full.")
        pass

    def dropItem(self):
        try:
            for i in range (len(self.inventory)):
                print("Slot#"+str(i)+" "+ self.inventory[i])
            choice = input("Select the item you want to drop. Enter 0 if you don't want to drop anything.\n")
            if choice > 0 and choice < len(self.inventory):
                if self.inventory[choice -1] == "Empty":
                    print("Wow you dropped nothing. Quite a big brain play.\n")
                else:
                    print("Youd dropped "+ self.inventory[choice-1] + ". It is no longer in your inventory.")
                    self.inventory[choice-1] = "Empty"

            elif choice == 0:
                print("No item was dropped")
            else:
                print("Inputs should be from 0 to "+ str(len(self.inventory))+ ".\n")

        except ValueError:
            print("Invalid input. Integer inputs only.\n")
        pass
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
    
# hello there stranger hehehxd
if __name__ == "__main__":
    p = player()
    p._init_()
    p.nameSet()
    p.itemAdd(item ="Fork")
    p.printInv()
    pass
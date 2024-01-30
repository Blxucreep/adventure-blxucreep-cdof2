import time

class Adventure:
    def __init__(self, player):
        self.player = player
        self.has_sword = False
        self.game_over = False
    
    def introduction(self):
        print("Welcome to this dungeon!")
        time.sleep(1)
        print("You find yourself in front of a mysterious door.")
        time.sleep(1)
        print("What action would you like to take?")
        time.sleep(1)

    def make_decision_door(self):
        decision = input("1. Open the door\n2. Examine the door\n3. Leave\nChoose an action: ")
        return decision
    
    def act_on_decision_door(self, decision):
        if decision == "1":
            print("You open the door and enter a dark room.")
            time.sleep(1)
            print("Suddenly, a creature appears in front of you!")
            self.battle()
        elif decision == "2":
            print("You examine the door and find a hidden key.")
            time.sleep(1)
            print("What do you want to do with the key?")
            time.sleep(1)
            print("1. Use the key to open the door\n2. Keep the key in your pocket\n3. Use the key to unlock a chest")
            action = input("Choose an action: ")
            if action == "1":
                print("You use the key to open the door and discover a secret room.")
                self.find_treasure()
            elif action == "2":
                print("You decide to keep the key in your pocket and leave.")
            elif action == "3":
                print("You use the key to unlock a chest and find a note.")
                self.check_note()
            else:
                print("Invalid action. Please choose a correct action.")
        elif decision == "3":
            print("You decide to leave. End of the adventure.")
            self.end_game()
        else:
            print("Invalid action. Please choose a correct action.")
    
    def battle(self):
        print("Battle with the creature!")
        time.sleep(1)
        print("You need a weapon to fight.")
        time.sleep(1)
    
        if self.has_sword:
            print("You use your sword to defeat the creature.")
            time.sleep(1)
            self.print_sword()
            print("You won the battle!")
            self.find_treasure()
            
        else:
            print("You don't have a weapon. The creature attacks, and you lose.")
            self.end_game()
    
    def find_treasure(self):
        print("Congratulations! You have discovered treasure in the secret room.")
        time.sleep(1)
        if not self.has_sword:
            print("You also find a sword!")
            self.gain_sword()
        print("You win the text adventure game. Thanks for playing, " + self.player.name + "!")
        self.game_over = True
    
    def end_game(self):
        print("End of the adventure. Thanks for playing.")
        self.game_over = True
    
    def gain_sword(self):
        self.has_sword = True
    def print_sword(self):
        print("       /| ________________")
        print("O|===|* >________________>")
        print("      \|")
   
    def check_note(self):
        print("You found a note inside the chest.")
        time.sleep(1)
        print("It says: 'To obtain the sword, press 5 and then 2.'")
        time.sleep(1)
        combination = input("Enter the combination: ")
        
        if combination == "5" and not self.has_sword:
            print("You hear a click and a hidden compartment opens, revealing a sword!")
            self.gain_sword()
        elif self.has_sword:
            print("You already have the sword.")
        else:
            print("Nothing happens.")
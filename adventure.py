import time

class Adventure:
    def __init__(self, player):
        self.player = player
    
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
            print("1. Use the key to open the door\n2. Keep the key in your pocket")
            action = input("Choose an action: ")
            if action == "1":
                print("You use the key to open the door and discover a secret room.")
                self.find_treasure()
            else:
                print("You decide to keep the key in your pocket and leave.")
        elif decision == "3":
            print("You decide to leave. End of the adventure.")
        else:
            print("Invalid action. Please choose a correct action.")
    
    def battle(self):
        print("Battle with the creature!")
        time.sleep(1)
        print("You need a weapon to fight.")
        time.sleep(1)
        
        if "sword" in self.player.inventory:
            print("You use your sword to defeat the creature.")
            time.sleep(1)
            print("You won the battle!")
            self.find_treasure()
        else:
            print("You don't have a weapon. The creature attacks, and you lose.")
            self.end_game()
    
    def find_treasure(self):
        print("Congratulations! You have discovered treasure in the secret room.")
        time.sleep(1)
        print("You win the text adventure game. Thanks for playing, " + self.player.name + "!")
    
    def end_game(self):
        print("End of the adventure. Thanks for playing.")
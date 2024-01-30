import time
from player import Player
from adventure import Adventure

def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    adv = Adventure(player)
    adv.introduction()
    
    while True:
        decision = adv.make_decision_door()
        adv.act_on_decision_door(decision)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()
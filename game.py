import time
from player import Player
from adventure import Adventure

def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    adv = Adventure(player)
    adv.introduction()

    while not adv.game_over:
        decision = adv.make_decision_door()
        adv.act_on_decision_door(decision)


if __name__ == "__main__":
    main()
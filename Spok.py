from multiprocessing import RLock
import random

game = True
game_variable = ["rock", "paper", "spok", "lizard", "scissors"]

def player_choise():
    while True:
        player_input = input("Your choise" + str(game_variable) + ": ")
        player_input.lower()
        if player_input in  game_variable:
            return player_input
        else:
            print("Invalid input:")

def check_continue():
    while True:
        repeat = input("Repeat (Y/N)? ")
        repeat.lower()
        if repeat == "y":
            return True
        elif repeat == "n":
            return False
        else:
            print('Invalid input: "' , repeat, '"')

def win_check(player_input, npc_choise):
    # print(player_input, npc_choise)
    dict_win_check = {
        "rock" : "paper",
        "paper" : "scissors",
        "scissors" : "rock",
        "lizard" : "rock",
        "lizard" : "scissors",        
        "paper" : "lizard",
        "spok" : "lizard",
        "spok" : "paper",
        "scissors" : "spok",
        "rock" :"spok"
    }
    if player_input == npc_choise:
        print("Nobody WINS ...")
    else:
        for incr in dict_win_check.items():
            print(incr, player_input, npc_choise)
            # if npc_choise == incr[0] and player_input == incr[1]:
            #     print("You LOOOOOOSE!!!")
            # elif player_input == incr[0] and npc_choise == incr[1]:
            #     print("You WIN!!!")
    return

while game:
    player_input = player_choise()
    npc_choise = random.choice(game_variable)
    print(player_input)
    print(npc_choise)
    win_check(player_input, npc_choise)
    game = check_continue()



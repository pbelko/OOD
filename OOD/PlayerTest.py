__author__ = 'Pat'

import math
import random
#####################################################################
# Testing methods
player_test_list = ['Tony', 'Collin', 'Baliga', 'Dan']
player_choice_test_list = ['Rock', 'Paper', 'Scissors']


def generate_test_results_one():
    for i in range(0, 50):
        player1 = player_test_list[math.floor(random.random() * 100) % 4]
        player2 = player_test_list[math.floor(random.random() * 100) % 4]

        while (player1 == player2):
            player2 = player_test_list[math.floor(random.random() * 100) % 4]

        notify(player1 + " playing " + player2)
        notify(player1 + " picked " + player_choice_test_list[math.floor(random.random() * 100) % 3])
        notify(player2 + " picked " + player_choice_test_list[math.floor(random.random() * 100) % 3])


def generate_test_results_two():
    player1 = "Tony"
    player2 = "Collin"

    for i in range(0, 50):
        notify(player1 + " playing " + player2)
        notify(player1 + " picked " + player_choice_test_list[math.floor(random.random() * 100) % 3])
        notify(player2 + " picked scissors")


generate_test_results_one()
me = "Pat"
other = player_test_list[math.floor(random.random() * 100) % 2]
notify(me + " playing " + other)
myPick = getMove()

print("Playing against: " + other)
print("Odds: ")
print("\t Rock: " + str(rockCut))
print("\t Paper: " + str(paperCut))
print("\t Scissors: " + str(1 - rockCut - paperCut))
print("I picked: " + getMove())

print(playerList)
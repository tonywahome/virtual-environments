import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print(RPS(2))

print("")
playerchoice = input("Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")



player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("Invalid choice. Please try again.")

computerchoice = random.choice([1, 2, 3])

print("")
print("You chose " + str(player) + ".")
print("Python chose " + str(computerchoice) + ".")
print("")

if (player == 1 and computerchoice == 3) or (player == 2 and computerchoice == 1) or (player == 3 and computerchoice == 2):
    print("you win🥳👏")
elif player == computerchoice:
    print("it's a tie🤝")
else:
    print("you lose😭")
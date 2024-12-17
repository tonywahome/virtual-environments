
import sys # Import the sys module to use the sys.exit() function.
import random # Import the random module to use the random.choice() function.
from enum import Enum # Import the Enum class from the enum module.

def play_rps():
    class RPS(Enum):
        """
        Enum class representing the possible moves in a Rock-Paper-Scissors game.

        Attributes:
            ROCK (int): Represents the move "Rock" with a value of 1.
            PAPER (int): Represents the move "Paper" with a value of 2.
            SCISSORS (int): Represents the move "Scissors" with a value of 3.
        """
        ROCK = 1
        PAPER = 2
        SCISSORS = 3
    
    
    playerchoice = input("\nEnter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")



    player = int(playerchoice)

    if player < 1 | player > 3:
        print("Invalid choice. Please try again.")
        return play_rps()
    computer = random.randint(1, 3)


    
    print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.','') + ".\n")
    
    if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        print("you win🥳👏")
    elif player == computer:
        print("it's a tie🤝")
    else:
        print("you lose😭")

    print("\nPlay again\n")
    playagain = input("\nPlay again? \nY for Yes or \nN for No:\n\n")
    if playagain.lower() not in ['y', 'n']:
        return play_rps()
    else:
        print("\nThanks for playing!")
        playagain = False

    sys.exit("Bye👋")

play_rps()

import random
import os
import time

def clear():
    os.system("clear")


def rps_instructions():

    print()
    print("Instructions for Rock ~ Paper ~ Scissors Game: ")
    print()
    print("Rock crushes Scissors")
    print("Scissors cut Paper")
    print("Paper covers Rock")
    print()

def rpsls_instructions():
    print()
    print("Instructions for Rock ~ Paper ~ Scissors ~ Lizard ~ Spock Game: ")
    print()
    print("Scissors cut Paper")
    print("Paper covers Rock")
    print("Rock crushes Lizard")
    print("Lizard poisons Spock")
    print("Spock smashes Scissors")
    print("Scissors decapitate Lizard")
    print("Lizard eats Paper")
    print("Paper disproves Spock")
    print("Spock vaporizes Rock")
    print("Rock crushes Scissors")
    print()

def rps():

        global rps_table
        global game_map
        global NameError

        while True:
            print("__________________________")
            print("\n")
            print("__________________________")
            print("Enter \"help\" for instructions")
            print("Enter \"Rock\", \"Paper\", \"Scissors\" to play")
            print("Enter \"exit\" to quit")
            print("___________________________")

            print()

            # player input
            inp = input("Enter Your Move: ")

            if inp.lower() == "help":
                clear()
                rps_instructions()
                continue
            
            elif inp.lower() == "exit":
                clear()
                break

            elif inp.lower() == "rock":
                player_move = 0
            
            elif inp.lower() == "paper":
                player_move = 1
            
            elif inp.lower() == "scissors":
                player_move = 2
            
            else:

                clear()
                print("Wrong Input!!")
                rps_instructions()
                continue
        
            print("Computer making a move....")

            print()
            time.sleep(2)

            # get the computer to move randomly
            comp_move = random.randint(0,2)

            # print the computer move

            print("Computer chooses", game_map[comp_move].upper())

            # find the winner
            winner = rps_table[player_move][comp_move]

            # declare the winner
            if winner == player_move:
                print(name, "Wins!!!\n")
            elif winner == comp_move:
                print("Computer Wins!!!\n")

            else:
                print("Tie Game")

            print()
            time.sleep(2)
            clear()

def rpsls():

    global rpsls_table
    global game_map
    global name 

    while True:

        print("________________________________")
        print("\t\tMenu")
        print("________________________________")
        print("Enter \"help\" for instructions")
        print("Enter \"Rock\", \"Paper\", \"Scissors\", \"Lizard\", \"Spock\" to play")
        print("Enter \"Exit\" to quit")
        print("________________________________")
        print()

        # Player input

        inp = input("Enter your move: ")

        if inp.lower() == "help":
            clear()
            rpsls_instructions()
            continue

        elif inp.lower() == "exit":
            clear()
            break
            
        elif inp.lower() == "rock":
            player_move = 0
        elif inp.lower() == "paper":
            player_move = 1
        elif inp.lower() == "scissors":
            player_move = 2
        elif inp.lower() == "lizard":
            player_move = 3
        elif inp.lower() == "spock":
            player_move = 4
        else:

            clear()
            print("Wrong Input!!")
            rps_instructions()
            continue

        print("Computer making a move....")

        comp_move = random.randint(0, 4)
        print()
        time.sleep(2)

        print("Computer chooses ", game_map[comp_move].upper())

        winner = rpsls_table[player_move][comp_move]
        print()
        if winner == player_move:
            print(name, " Wins!!!\n")
        elif winner == comp_move:
            print("Computer Wins!!!")

        else:
            print("Tie Game")
            time.sleep(2)
            clear()

if __name__ == '__main__':

    # the mapping between moves and numbers
    game_map = {0:"rock", 1:"paper", 2:"scissors", 3:"lisard", 4:"Spock"}

    # win-lose matrix for traditional game
    rps_table = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]

    # win-lose matrix for new version of game
    rpsls_table = [[-1, 1, 0, 0, 4],[1, -1, 2, 3, 1], [0, 2, -1, 2, 4], [0, 3, 2, -1, 3], [4, 1, 4, 3, -1]]

    name = input("Enter your name: ")
    
    # game loop

    while True:

        print()
        print("Let's Play!!!")
        print("Which version of Rock-Paper-Scissors?")
        print("Enter 1 to play Rock-Paper-Scissors")
        print("Enter 2 to play Rock-Paper-Scissors-Lizard-Spock")
        print("Enter 3 to quit")
        print() 

        try:

            choice = int(input("Enter your choice = "))
        
        except ValueError:
            clear()
            print("Wrong Choice")
            continue

        # traditional game
        if choice == 1:
            rps()

        # new version
        if choice == 2:
            rpsls()

        # quit the game
        if choice == 3:
            break
            
        # incorrect choice
        else:
            clear()
            print("Wrong Choice, Read instructions carefully")





        




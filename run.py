from random import randint


def start_game():
    """
    Initiates a new game. Allows the player to set the board size and the
    number of ships in the game. Initialises the boards and resets the scores.
    """

    board_size = 5
    amount_ships = 4
    print("-----------------------------------")
    print("      Welcome to BATTLESHIPS!!     ")
    print(f" Board Size: {board_size}. Number of Ships: {amount_ships}")
    print(" Top left corner is row: 0, col: 0")
    print("-----------------------------------")
    player_name = input("What is your name? \n")
    print("-----------------------------------")

start_game()


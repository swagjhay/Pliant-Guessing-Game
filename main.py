#!/usr/bin/env python3
from game import single_player, multiplayer
import time

def play_again():
    while True:
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice.lower() == "y":
            return True
        elif choice.lower() == "n":
            print("Exiting the game ...")
            time.sleep(1)
            print("Thanks for playing! Goodbye!")
            return False

def main():
    while True:
        try:
            print("Welcome to Pliant Guessing Game ")
            print("1. Single Player")
            print("2. Multiplayer")
            print("3. Exit")
        except ValueError:
            print("Please enter a valid number")
        choice = int(input("Choose an option: ")) 
        if choice == 1:
            min_number, max_number, close_range = game_mode()
            print(single_player(min_number, max_number, close_range))
            if not play_again():
                break
        elif choice == 2:
            min_number, max_number, close_range = game_mode()
            print(multiplayer(min_number, max_number, close_range))
            if not play_again():
                break
        elif choice == 3:
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
def game_mode():
    while True:
        try:
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            print("4. Insane")
            usr_choice= int(input("Choose a game mode: "))
        except ValueError:
            print("Please enter a valid number")
        if usr_choice == 1:
            return 1,50,3
        elif usr_choice == 2:
            return 1,500,5
        elif usr_choice == 3:
            return 1,1000,10
        elif usr_choice == 4:
            return 1,5000,15
        else:
            print("Invalid choice.")
    
if __name__ == "__main__":
    main()

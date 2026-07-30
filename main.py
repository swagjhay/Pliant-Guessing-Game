#!/usr/bin/env python3
from game import single_player, multiplayer

def main():
    while True:
        print("Welcome to Pliant Guessing Game ")
        print("1. Single Player")
        print("2. Multiplayer")
        print("3. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            single_player()
        elif choice == "2":
            multiplayer()
        elif choice == "3":
            print("Exiting the game. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
    
if __name__ == "__main__":
    main()
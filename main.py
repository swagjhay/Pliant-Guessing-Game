#!/usr/bin/env python3
from game import single_player, multiplayer
import time
import json


def load_high_scores():
    with open("highscores.json", "r") as file:
        return json.load(file)
    
def main():
    print(f" -----------------------------------")
    print(f"|  Welcome to Pliant Guessing Game  |")
    print(f" -----------------------------------")
    while True:
        print("[1] Single Player")
        print("[2] Multiplayer")
        print("[3] High Scores")
        print("[4] Exit")
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Please enter a valid number")
            continue
        if choice == 1:
            min_number, max_number, close_range = game_mode()
            attempts, player_name = single_player(min_number, max_number, close_range)
            score = max(0, 100 - (attempts - 1) * 10)  # Calculate score based on attempts
            print("\n ========== Game Over ========")
            print("    congratulations!")
            print(f"  You found the lucky number in {attempts} attempts")
            print(f"  Your score is: {score}")
            print("  ===============================")
            if not play_again():
                break
        elif choice == 2:
            min_number, max_number, close_range = game_mode()
            winner,attempts = multiplayer(min_number, max_number, close_range)
            print("\n========== FINAL SCOREBOARD ==========")
            print(f"{'Player':<15}{'Attempts':<10}{'Result'}")
            print("--------------------------------------")

            for player, player_attempts in attempts.items():
                if player == winner:
                    result = "🏆 WINNER"
                else:
                    result = ""

                print(f"{player:<15}{player_attempts:<10}{result}")

            print("======================================")
            if not play_again():
                break
        elif choice == 3:
            print("\n========== HIGH SCORES ==========")
            print("Single Player")
            print('---------------------')
            print("No scores yet. Play the game to set a high score!")
            print()
            print("Multiplayer")
            print('---------------------')
            print("No scores yet. Play the game to set a high score!")
            print("=================================")
            break
        elif choice == 4:
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

if __name__ == "__main__":
    main()

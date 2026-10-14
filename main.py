#!/usr/bin/env python3
from game import single_player, multiplayer, calculate_score
from pathlib import Path
import time
import json

# Always look for the file next to main.py, wherever the game is run from
HIGH_SCORES_FILE = Path(__file__).parent / "highscores.json"
MAX_ENTRIES = 3  # keep the top 3 in each leaderboard
MODES = ["single_player", "multiplayer"]

DIFFICULTIES = {
    # penalty = points lost for each attempt after the first
    "1": {"name": "Easy",   "min": 1, "max": 50,   "close_range": 3,  "penalty": 10},
    "2": {"name": "Medium", "min": 1, "max": 500,  "close_range": 5,  "penalty": 6},
    "3": {"name": "Hard",   "min": 1, "max": 1000, "close_range": 10, "penalty": 5},
    "4": {"name": "Insane", "min": 1, "max": 5000, "close_range": 15, "penalty": 4},
}

def empty_high_scores():
    # {"single_player": {"Easy": [], ...}, "multiplayer": {"Easy": [], ...}}
    return {
        mode: {level["name"]: [] for level in DIFFICULTIES.values()}
        for mode in MODES
    }

def load_high_scores():
    try:
        with open(HIGH_SCORES_FILE, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # File missing, empty or corrupted: start fresh instead of crashing
        return empty_high_scores()
 
    # Start from a complete empty structure, then copy in whatever valid
    # leaderboards the file has. Anything broken or missing stays empty.
    high_scores = empty_high_scores()
    if not isinstance(data, dict):
        return high_scores
    for mode in high_scores:
        mode_data = data.get(mode)
        if not isinstance(mode_data, dict):
            continue
        for difficulty in high_scores[mode]:
            saved = mode_data.get(difficulty)
            if isinstance(saved, list):
                high_scores[mode][difficulty] = saved
    return high_scores

def save_high_score(mode, difficulty, name, score, attempts):
    """Add a result, keep only the top 3, and return True if it made the board."""
    high_scores = load_high_scores()
    board = high_scores[mode][difficulty]
 
    new_entry = {"name": name, "score": score, "attempts": attempts}
    board.append(new_entry)
    # Highest score first. sort() keeps the original order for ties,
    # so an older score stays ahead of a new score that only matches it.
    board.sort(key=lambda entry: entry.get("score", 0), reverse=True)
    top_entries = board[:MAX_ENTRIES]
    high_scores[mode][difficulty] = top_entries
 
    with open(HIGH_SCORES_FILE, "w") as file:
        json.dump(high_scores, file, indent=4)
 
    return any(entry is new_entry for entry in top_entries)

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
            level = game_mode()
            attempts, player_name = single_player(level["min"], level["max"], level["close_range"])
            score = calculate_score(attempts, level["penalty"])
            print("\n ========== Game Over ========")
            print("    congratulations!")
            print(f"  You found the lucky number in {attempts} attempts")
            print(f"  Your score is: {score}")
            print("  ===============================")
            if score > 0 and save_high_score("single_player", level["name"], player_name, score, attempts):
                print(f"  New {level['name']} high score! Check the High Scores menu.")
            if not play_again():
                break
        elif choice == 2:
            level = game_mode()
            winner, attempts = multiplayer(level["min"], level["max"], level["close_range"])
            winner_attempts = attempts[winner]
            score = calculate_score(winner_attempts, level["penalty"])
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
            print(f"{winner} scores {score} points")
            if score > 0 and save_high_score("multiplayer", level["name"], winner, score, winner_attempts):
                print(f"New {level['name']} multiplayer high score!")
            if not play_again():
                break
        elif choice == 3:
            show_high_scores()
        elif choice == 4:
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
def print_leaderboard(title, entries):
    print(f"\n{title}")
    print("-" * 37)
    if not entries:
        print("No scores yet. Play the game to set a high score!")
        return
    print(f"{'Rank':<6}{'Name':<15}{'Score':<8}{'Attempts'}")
    for rank, entry in enumerate(entries, start=1):
        name = str(entry.get("name", "?"))[:14]  # long names would break the columns
        print(f"{rank:<6}{name:<15}{entry.get('score', 0):<8}{entry.get('attempts', '-')}")


def show_high_scores():
    high_scores = load_high_scores()
    while True:
        print("\n========== HIGH SCORES ==========")
        for number, level in DIFFICULTIES.items():
            print(f"{number}. {level['name']}")
        print("5. Back to main menu")
        choice = input("Choose a game mode: ").strip()
        if choice == "5":
            return
        if choice not in DIFFICULTIES:
            print("Invalid choice. Please enter a number from 1 to 5.")
            continue
        difficulty = DIFFICULTIES[choice]["name"]
        print(f"\n----- {difficulty} -----")
        print_leaderboard("Single Player", high_scores["single_player"][difficulty])
        print_leaderboard("Multiplayer", high_scores["multiplayer"][difficulty])
        print("=================================")
                  
def game_mode():
    while True:
        for number, level in DIFFICULTIES.items():
            print(f"{number}. {level['name']}")
        choice = input("Choose a game mode: ").strip()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print("Invalid choice. Please enter a number from 1 to 4.")
    

def play_again():
    while True:
        choice = input("Do you want to play again? (y/n): ").strip().lower()
        if choice == "y":
            return True
        elif choice == "n":
            print("Exiting the game ...")
            time.sleep(1)
            print("Thanks for playing! Goodbye!")
            return False
        else:
            print("Please type y or n.")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGame closed. Goodbye!")

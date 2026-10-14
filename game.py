#!/usr/bin/env python3
import random
 
def get_name(prompt):
    """Ask until the player types a name that isn't blank."""
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("Name cannot be empty. Please try again.")

def calculate_score(attempts, penalty):
    """1 attempt = 100 points, each extra attempt costs `penalty`, never below 0."""
    return max(0, 100 - (attempts - 1) * penalty)
 
def single_player(min_number, max_number, close_range):
    attempt = 0
    guessed = set()  # numbers already tried this game
    secret_number = random.randrange(min_number, max_number + 1)
    player_name = get_name("Enter your name: ")
    while True:
        try:
            guess = int(input(f"Guess a number ({min_number}-{max_number}): "))
            #check if the guess is within the range
            if guess < min_number or guess > max_number:
                print(f"Please enter a number between {min_number} and {max_number}")
                continue
            # a repeated guess is a mistake, so warn and don't count it
            if guess in guessed:
                print(f"You already guessed {guess}. Try a different number.")
                continue
            guessed.add(guess)
            #attempts counter starts the moment the user enters a valid number
            attempt += 1
            #if the user guesses the secret number, it will return a message with the number of attempts it took to guess correctly
            if guess == secret_number:
                return attempt, player_name
            #let's you know if your close to the secret number
            #the user has to figure if it is a higher or lower number
            elif abs(guess - secret_number) <= close_range:
                print("You are very close, try again")
            #gives the user a hint if their guess is higher or lower than the secret number
            elif guess < secret_number:
                print("Enter a higher number")
            elif guess > secret_number:
                print("Enter a lower number")
        except ValueError:
            print("Please enter a valid number")
            continue
 
def multiplayer(min_number, max_number, close_range):
    secret_number = random.randrange(min_number, max_number + 1)
    # get the number of players (validate input)
    while True:
        try:
            num_players = int(input("Enter the number of players: "))
            if num_players < 2 or num_players > 10:
                print("Please enter between 2 and 10 players")
                continue
            break
        except ValueError:
            print("Please enter a valid number")
    #initialize an empty list to store the names of the players
    players = []
    #get the names of the players
    for i in range(num_players):
        name = get_name(f"Enter the name of player {i + 1}: ")
        # if the name is already taken (ignoring capitals), add a number to it
        original_name = name
        counter = 2
        taken = [player.lower() for player in players]
        while name.lower() in taken:
            name = f"{original_name}{counter}"
            counter += 1
        players.append(name)
    #track each player's attempts in a dictionary.
    attempts = {player: 0 for player in players}
    turn = 0 # keep track of whose turn it is
    guessed = set()  # numbers any player has already tried
 
    while True:
        # get the current player based on the turn
        current_player = players[turn % num_players]
        try:
            guess = int(input(f"{current_player}, guess a number ({min_number}-{max_number}): "))
            #check if the number is within the range
            if guess < min_number or guess > max_number:
                print(f"Please enter a number between {min_number} and {max_number}")
                continue
            # same player tries again: continue skips "turn += 1" below
            if guess in guessed:
                print(f"{guess} has already been guessed. Try a different number.")
                continue
            guessed.add(guess)
            #increment the current player's attempts
            attempts[current_player] += 1
            #if the user guesses the secret number, it will return a message with the number of attempts it took to guess correctly
            if guess == secret_number:
                return current_player, attempts
            #let's you know if your close to the secret number
            #the user has to figure if it is a higher or lower number
            elif abs(guess - secret_number) <= close_range:
                print("You are very close, try again")
            #gives the user a hint if their guess is higher or lower than the secret number
            elif guess < secret_number:
                print("Enter a higher number")
            elif guess > secret_number:
                print("Enter a lower number")
            turn += 1
        except ValueError:
            print("Please enter a valid number")
            continue

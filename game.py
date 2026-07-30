#!usr/bin/env python3
import random


min_number = 1
max_number = 50
close_range = 3
secret_number = random.randrange(min_number, max_number + 1)

def single_player():
    attempt = 0
    while True:
        try:
            guess = int(input(f"Guess a number ({min_number}-{max_number}): "))
            #check if the guess is within the range
            if guess < min_number or guess > max_number:
                print(f"Please enter a number between {min_number} and {max_number}")
                continue
            #attempts counter starts the moment the user enters a valid number
            attempt += 1
            #if the user guesses the secret number, it will return a message with the number of attempts it took to guess correctly
            if guess == secret_number:
                return f"That was correct!!! You got the lucky number in {attempt} attempts"
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

def multiplayer():
    # get the number of players (validate input)
    while True:
        try:
            num_players = int(input("Enter the number of players: "))
            if num_players < 2:
                print("There must be at least 2 players")
                continue
            break
        except ValueError:
            print("Please enter a valid number")
    #initialize an empty list to store the names of the players
    players = []
    #get the names of the players
    for i in range(num_players):
        name = input(f"Enter the name of player{i + 1}: ")
        #if name is already in the list, ask for a different name
        original_name = name
        counter = 2
        while name in players:
            name = f"{original_name}{counter}"
            counter += 1
        players.append(name)
    #track each player's attempts in a dictionary.
    attempts = {player: 0 for player in players}
    turn = 0 # keep track of whose turn it is

    while True:
        # get the current player based on the turn
        current_player = players[turn % num_players]
        try:
            guess = int(input(f"{current_player}, guess a number ({min_number}-{max_number}): "))
            #check if the number is within the range
            if guess < min_number or guess > max_number:
                print(f"Please enter a number between {min_number} and {max_number}")
                continue
            #increment the current player's attempts
            attempts[current_player] += 1
            #if the user guesses the secret number, it will return a message with the number of attempts it took to guess correctly
            if guess == secret_number:
                return f"That was correct!!! {current_player} got the lucky number in {attempts[current_player]} attempts"
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
#main function to run the single player game as of now, will be updated to include multiplayer in the future
def main():
    print(single_player())

if __name__ == '__main__':
    main()

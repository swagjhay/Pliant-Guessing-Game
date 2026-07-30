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
#main function to run the single player game as of now, will be updated to include multiplayer in the future
def main():
    print(single_player())

if __name__ == '__main__':
    main()
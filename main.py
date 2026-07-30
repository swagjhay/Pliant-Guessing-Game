import random
min_number = 1
max_number = 50
close_range = 5
secret_number = random.randrange(min_number, max_number + 1)

def single_player():
    attempt = 0
    while True:
        try:
            guess = int(input(f"Guess a number ({min_number}-{max_number}): "))
            attempt += 1
            if abs(guess - secret_number) <= close_range:
                print("You are very close, try again")
            elif guess < secret_number:
                print("Enter a higher number")
            elif guess > secret_number:
                print("Enter a lower number")
            
            else:
                return f"That was correct!!! You got the lucky number in {attempt} attempts"
        except ValueError:
            print("Please enter a valid number")
            continue
        
def main():
    print(single_player())

if __name__ == '__main__':
    main()
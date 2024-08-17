import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        # Get the user's guess
        guess = input("Enter your guess (or type 'exit' to quit): ")
        
        # Allow the user to exit the game
        if guess.lower() == 'exit':
            print(f"The secret number was {secret_number}. Thanks for playing!")
            break

        # Convert the guess to an integer
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        # Check the guess
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()

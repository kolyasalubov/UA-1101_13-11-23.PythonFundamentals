import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Set the number of attempts
max_attempts = 10
attempts = 0

# Game loop
while attempts < max_attempts:
    # Prompt the user for a guess
    guess = int(input("Guess a number from 1 to 100): "))

    # Check if the guessed number is correct
    if guess == secret_number:
        print("Congratulations! You guessed the number.")
        break
    elif guess < secret_number:
        print("The secret number is greater than your guess.")
    else:
        print("The secret number is less than your guess.")

    # Increment the number of attempts
    attempts += 1

# Check if the user ran out of attempts
if attempts == max_attempts:
    print("Sorry, you ran out of attempts. The secret number was", secret_number)

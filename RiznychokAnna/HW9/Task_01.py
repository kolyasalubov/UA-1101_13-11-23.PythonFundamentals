from random import randint

def guess_number():
    
    secret_number = randint(1, 100)
    
    attempts = 0
    max_attempts = 10

    print("Welcome to the Guessing Game!\n")
    print(f"Try to guess the number between 1 and 100 in {max_attempts} attempts.\n")

    while attempts < max_attempts:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

    if attempts == max_attempts:
        print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {secret_number}.")

guess_number()

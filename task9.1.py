import random

def guessing_game():

    secret_number = random.randint(1, 100)


    attempts_left = 10

    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    while attempts_left > 0:

        user_guess = int(input(f"Enter your guess (Attempts left: {attempts_left}): "))

        if user_guess == secret_number:
            print("Congratulations! You guessed the number.")
            break
        elif user_guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")


        attempts_left -= 1

    if attempts_left == 0:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    guessing_game()

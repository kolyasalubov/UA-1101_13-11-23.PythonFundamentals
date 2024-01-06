import random

def guess_the_number():
  
    secret_number = random.randint(1, 100)
    
    attempts = 10
    
    print("Welcome to the Guess the Number game!")
    print("Try to guess the number between 1 and 100.")

    while attempts > 0:
        guess = int(input("Enter your guess: "))
        
        if guess == secret_number:
            print("Congratulations! You guessed the number!")
            break
        elif guess < secret_number:
            print("Try again. The secret number is greater.")
        else:
            print("Try again. The secret number is smaller.")

        attempts -= 1
        print(f"Attempts left: {attempts}")

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    guess_the_number()
    

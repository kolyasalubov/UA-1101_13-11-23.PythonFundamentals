from random import randint

TOP_BORDER = 100

def check_if_lost(count):
    if count > 10:
        print("You lost.")


def start_game():
    user_name = input('Hello! What is your name?\n')

    number = randint(1, TOP_BORDER)

    print(f'I am thinking of a number between 1 and {TOP_BORDER}. \
You have 10 tries - use them wise. Good luck!')

    counter = 1

    while counter < 11:

        guess_number = int(
            input(f'Attempt №{counter}. Take a guess! Enter your number: '))

        if guess_number == number:
            print(f'Good job, {user_name}! You are a winner!')
            break

        elif guess_number < number:
            print('Your number is less.')
            counter += 1
            check_if_lost(counter)

        elif guess_number > number:
            print('Your number is more.')
            counter += 1
            check_if_lost(counter)
      
start_game()
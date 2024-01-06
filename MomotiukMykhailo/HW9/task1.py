from random import randint

number = randint(1, 100)


def randomizer():
    print(f'Guess a number between 1 and 100')

    counter = 1

    while counter < 11:

        guess_number = int(input(f'Attempt № {counter}. Enter your number: '))

        if guess_number == number:
            print(f'You are correct!')
            break

        elif guess_number < number:
            print('Your number is less, try again.')
            counter += 1

        elif guess_number > number:
            print('Your number is more, try again.')
            counter += 1

        if counter == 11:
            print("Better luck next time!")


randomizer()
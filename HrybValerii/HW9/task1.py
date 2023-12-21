from random import randint
number_of_attempts = 10
lower_boundary = 1
upper_boundary = 100
number_to_guess = randint(lower_boundary, upper_boundary)
for _ in range(number_of_attempts):
    guess_num = int(input(f"Guess the number from {lower_boundary} to {upper_boundary}: "))
    if guess_num == number_to_guess:
        print(f"You won! The number was {number_to_guess}")
        break
    elif number_to_guess > guess_num:
        print('The number is more, try again.')
    else:
        print('The number is less, try again.')
    print()
else:
    print(f"""There's no attempts left. You've lost(
The number was {number_to_guess}""")

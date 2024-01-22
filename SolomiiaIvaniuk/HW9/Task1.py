from random import randint
number_of_attempts = 10
lower_boundary = 1
upper_boundary = 100
number_to_guess = randint(lower_boundary, upper_boundary)
for _ in range(number_of_attempts):
    guess_number = int(input(f"Guess the number from {lower_boundary} to {upper_boundary}: "))
    if guess_number == number_to_guess:
        print(f"You won! The number was {number_to_guess}")
        break
    elif number_to_guess > guess_number:
        print("Try a higher number.")
    else:
        print("Try a lower number.")
    print()
else:
    print(f"""Sorry,you usrd all number( Try again!{number_to_guess}""")
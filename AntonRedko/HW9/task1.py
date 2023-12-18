from random import randint


def guess_number():
    name_player = input("Enter your name: ")

    programm_hidden_number = randint(1, 100)

    i = 0
    while i < 10:
        hidden_number = int(input("Guess your number: "))
        if hidden_number == programm_hidden_number:
            print("you're right")
            break
        elif hidden_number < programm_hidden_number:
            print("your number are less")
            i += 1
        elif hidden_number > programm_hidden_number:
            print("your number are more")
            i += 1

        if i == 10:
            print("youre wasted all chances")


guess_number()

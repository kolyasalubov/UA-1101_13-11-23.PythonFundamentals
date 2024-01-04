from random import randint

count = 0

number = randint(1, 100)


while count < 10:
    count += 1
    print(f"You are using your {count} attempt")
    user = input("Enter number: ")
    number = str(number)

    if user == number:
        print("Congratulations!")
        break
    elif user < number:
        print("Enter a higher number ")
    elif user > number:
        print("Enter a lower number ")

    if count == 10:
        print("You used all your 10 attempts")

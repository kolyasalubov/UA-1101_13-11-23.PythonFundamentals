import random

# Генеруємо випадкове число від 1 до 100
number = random.randint(1, 100)

# Ітеруємося 10 разів, щоб користувач відгадав число
for i in range(10):
    # Просимо користувача ввести число
    guess = int(input("Введіть число: "))

    # Порівнюємо вгадане число з випадковим
    if guess == number:
        # Вітаємо користувача, якщо він вгадав число
        print("Вітаю! Ви вгадали число!")
        break
    elif guess < number:
        # Підказуємо користувачеві, що число більше
        print("Ваше число менше.")
    else:
        # Підказуємо користувачеві, що число менше
        print("Ваше число більше.")

# Якщо користувач не вгадав число за 10 спроб
if i == 9:
    print("Ви програли! Правильне число:", number)
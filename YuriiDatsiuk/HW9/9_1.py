from random import randint

MIN = 1
MAX = 100
COUNT_TRY = 10

random_number = randint(MIN, MAX)

win = False
for _ in range(1, COUNT_TRY+1):

    user_number_s = input(f'Enter number between {MIN} - {MAX} ')

    if not user_number_s.isdigit():
        print('type only integer number')
        break

    user_number = int(user_number_s)

    if user_number == random_number:
        win = True
        break
    else:
        if user_number > random_number:
            print('its smaller then', user_number)
        else:
            print('its bigger then', user_number)

print('GREAT' if win else 'TRY AGAIN')
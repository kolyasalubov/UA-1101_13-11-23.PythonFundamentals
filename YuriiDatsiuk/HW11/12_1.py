day_of_week = input('Enter number day of the week ')
result = ''
days_week = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}

try:
    day_of_week = int(day_of_week)
    if day_of_week > 7:
        raise Exception('its cant be bigger than 7')

    result = days_week.get(day_of_week)
except ValueError as e:
    print('its not integer.', e)
except Exception as e:
    print('Exeption.', e)
else:
    print(result)

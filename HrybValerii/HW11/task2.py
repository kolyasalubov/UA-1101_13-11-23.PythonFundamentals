days = {'1': 'Monday', '2': 'Tuesday', '3': 'Wednesday', '4': 'Thursday', '5': 'Friday', '6': 'Saturday', '7': 'Sunday'}
error_message = 'You should enter a positive number that doesn\'t exceed 7'
try:
    number = input('Enter a day number: ')
    print(days[number])
except KeyError as e:
    print(error_message)
except Exception as e:
    print(f'Error: {e}')


# alternative solution
number2 = input('Enter a day number: ')
print(days.get(number2, error_message))

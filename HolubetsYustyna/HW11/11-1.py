class NegAgeError(Exception):

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr('My repr: Age cannot be a negative number')


def check_age(inp_age):
    if inp_age < 0:
        raise NegAgeError('Age must be a positive number')
    elif inp_age == 0:
        print(f'{inp_age}: Your age is an even number but I doubt you\'re an infant \U0001F611')
    elif inp_age % 2:
        print(f'{inp_age}: Your age is an odd number')
    else:
        print(f'{inp_age}: Your age is an even number')
    if inp_age > 120:
        print('What a long life you\'ve lived! \U0001F44D ...\U0001F611\U0001F611\U0001F611')


try:
    user_age = int(input('Please enter your age: '))
    check_age(user_age)
except NegAgeError as e:
    print(f'Error: {e.data}')
except TypeError as e:
    print(f'Error: {e}')
except ValueError as e:
    print(f'Error: {e}')
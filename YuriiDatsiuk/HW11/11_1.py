

def check_age(age):
    try:
        age = int(age)
    except ValueError as e:
        print('its not an integer.', e)
        return

    if age < 0:
        raise ValueError('entered a negative number')
    else:
        if age%2 == 0:
            print('age is even')
        else:
            print('age is odd')


age = input('Enter your age ')
try:
    check_age(age)
except Exception as e:
    print(e)

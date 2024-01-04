def ask_age():
    age = int(input("Enter your age: "))
    if age > 0:
        return age
    raise ValueError('Entered number is not positive')


try:
    user_age = ask_age()
    if user_age % 2:
        print('Your age is odd')
    else:
        print('Your age is even')
except ValueError as e:
    print(f'Error: {e}')
except Exception as e:
    print(f'Error: {e}')


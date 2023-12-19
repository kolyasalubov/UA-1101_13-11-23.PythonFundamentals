try:
    age = int(input('Your age: '))
    if age < 0:
        raise ValueError('Age should be positive')
except ValueError as e:
    print('Age should be positive')

else:
    if age % 2 == 0:
        print('Age is even.')
    else:
        print('Age is odd.')
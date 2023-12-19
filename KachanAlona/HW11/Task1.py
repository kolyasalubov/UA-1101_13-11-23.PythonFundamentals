def age_checker():
    try:
        age = int(input('Your age: '))
        if age < 0:
            raise ValueError('Age should be positive')
    except ValueError as e:
        print(e)

    else:
        if age % 2 == 0:
            print('Age is even.')
        else:
            print('Age is odd.')


age_checker()

login = input('Enter your login: ')

while login != 'First':
    print('Error! Try another login.')
    login = input('Enter your login: ')
else:
    print(f"Congrats! Your login is {login}")
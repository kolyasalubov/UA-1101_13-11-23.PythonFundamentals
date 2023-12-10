login = None
while login != 'First':
    login = input("Enter login: ")

    match login:
        case 'First':
            print('Hello First! Welcome!')
        case _:
            print('Incorrect login, try again.')
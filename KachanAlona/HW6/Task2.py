login_from_user = input('Please enter your login: ')
correct_login = "First"
while login_from_user.capitalize() != correct_login:
    login_from_user = input(f'Sorry, the login {login_from_user} is wrong. Try again: ')
else:
    print(f'Nice to meet you, {correct_login}!')

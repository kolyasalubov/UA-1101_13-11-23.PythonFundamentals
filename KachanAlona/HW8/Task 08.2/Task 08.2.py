import re

def password_checker():
    password_from_user = input('Enter password: ')
    regex = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[$#@]).{6,16}$"
    if re.findall(regex, password_from_user):
        print("Your password has saved.")
    else:
        print("Your password doesn't valid. Try again.")
        password_checker()

password_checker()

import re

def is_valid_password(password):
    
    if len(password) < 6:
        return False

    if len(password) > 16:
        return False

    if not re.search("[a-z]", password):
        return False

    if not re.search("[A-Z]", password):
        return False

    if not re.search("[0-9]", password):
        return False

    if not re.search("[$#@]", password):
        return False

    return True

user_password = input("Enter a password: ")

if is_valid_password(user_password):
    print("Password is valid.")
else:
    print("Password is invalid. Please follow the specified criteria.")
import re

def is_valid_password(password):

    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[\^#@]).{6,16}$'

    if re.match(pattern, password):
        return True
    else:
        return False

user_password = input("Enter your password: ")

if is_valid_password(user_password):
    print("Valid password.")
else:
    print("Invalid password. Please make sure it meets the specified criteria.")

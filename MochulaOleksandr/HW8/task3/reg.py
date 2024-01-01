import re
def check_password_validity(password):
    if len(password) < 6 or len(password) > 16:
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"\d", password):
        return False

    if not re.search(r"[$#@]", password):
        return False

    return True

# Test the password validity
password = input("Enter a password: ")
if check_password_validity(password):
    print("Password is valid.")
else:
    print("Password is invalid.")
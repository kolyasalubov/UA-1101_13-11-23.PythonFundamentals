import re

def valid_password(password):
    if len(password) >= 6 and len(password) <= 16:
        if re.search("[a-z]", password):
            if re.search("[A-Z]", password):
                if re.search("[0-9]", password):
                    if re.search("[$#@]", password):
                        return True
                    else:
                        return False, "Password must contain at least one of the special characters: $, #, @"
                else:
                    return False, "Password must contain at least one digit (0-9)"
            else:
                return False, "Password must contain at least one uppercase letter"
        else:
            return False, "Password must contain at least one lowercase letter"
    else:
        return False, "Password length must be between 6 and 16 characters"

user_password = input("Enter your password: ")
result = valid_password(user_password)

if result is True:
    print("Password is valid.")
else:
    print("Invalid password:", result[1])
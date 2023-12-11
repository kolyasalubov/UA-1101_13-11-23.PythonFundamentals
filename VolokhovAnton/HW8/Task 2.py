import re

def check_password_validity(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@]).{6,16}$"
    return "Valid password" if re.match(pattern, password) else "Invalid password"

# Take password input from the user
user_password = input("Enter your password: ")

# Check the validity of the password
result = check_password_validity(user_password)
print(result)

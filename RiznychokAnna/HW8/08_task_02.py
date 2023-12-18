import re

CHR = "Password must contain at least 1 character from [$#@!]"
PLD = "Password must contain at least 1 digit [0-9]"
PUL = "Password must contain at least 1 uppercase letter [A-Z]"
PLL = "Password must contain at least 1 lowercase letter [a-z]"
PLCH = "Password length must be between 6 and 16 characters"

def is_valid_password(password):
    # Check minimum and maximum length
    if 6 <= len(password) <= 16:
        # Check for at least 1 lowercase letter
        if re.search(r'[a-z]', password):
            # Check for at least 1 uppercase letter
            if re.search(r'[A-Z]', password):
                # Check for at least 1 digit
                if re.search(r'[0-9]', password):
                    # Check for at least 1 character from [$#@]
                    if re.search(r'[$#@!]', password):
                        return True
                    else:
                        print(CHR)
                else:
                    print(PLD)
            else:
                print(PUL)
        else:
            print(PLL)
    else:
        print(PLCH)

    return False

# Get password input from the user
user_password = input("Enter your password: ")

# Check password validity
if is_valid_password(user_password):
    print("Password is valid!")
else:
    print("Invalid password. Please try again.")

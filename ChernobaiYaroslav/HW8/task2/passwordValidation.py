from re import compile, match

# Check for the entire string:
# '^' - start of the string, '$' -  end of the string

# [a-z] - any character in the range between a-z
# [A-Z] - any character in the range between A-Z
# \d - the same as [0-9], any digit
# [#$@] - any character from the mentioned list
# . - any single character
# * - 0 or more occurance of a character before in a string
# () - to check independently each requirement
# .{start, end} - to check for the length of a string

def passValidation(password):
    pattern = compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#$@]).{6,16}$")
    return bool(pattern.match(password))



print("""Your password:
- has to be a minimum of 6 characters and a maximum of 16 characters in length;
- has to contain at least 1 letter between [a-z] and 1 letter between [A-Z];
- has to contain at least 1 number between [0-9];
- has to contain at least 1 character from [$#@];
""")

while True:
    user_password = input("Enter your password: ")

    if passValidation(user_password):
        print("Your password is valid.\n")
        break
    else:
        print("Your password is invalid.\n")

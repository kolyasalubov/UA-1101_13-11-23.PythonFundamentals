from re import compile, match


def valid_password(input):
    result = compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#$@]).{6,16}$")
    return bool(result.match(input))


print('''Before writing your password read this attentively: 
at least 1 letter between [a-z] and 1 letter between [A-Z];
at least 1 number between [0-9];
at least 1 character from [$#@];
Minimum length 6 characters;
Maximum length 16 characters''')

user = input("Enter your password: ")

if valid_password(user):
    print("Your password is correct")
else:
    print("You made some mistakes")
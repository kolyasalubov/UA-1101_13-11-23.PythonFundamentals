import re

MESSAGES = [
'Password successfully created',
'Please make sure to include',
'at least one small letter',
'at least one capital letter', 
'at least one number 0..9',
'at least one character $#@',
'Your password is too short. Min length: 6',
'Your password is too long. Max length: 16'
]

user_password_inp = input('Create a password:\nAt least one capital and one small letter\n\
                    At least one number 0..9\nAt least one character\nOf 6 to 16 characters length\n')


check_pass = re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[#$%]).{6,16}$', user_password_inp)

if check_pass:
    print(MESSAGES[0])
else:

    if re.match('^((?![a-z]).)*$', user_password_inp):
        print(MESSAGES[1], MESSAGES[2])
    
    if re.match('^((?![A-Z]).)*$', user_password_inp):
        print(MESSAGES[1], MESSAGES[3])

    if re.match('^((?![0-9]).)*$', user_password_inp):
        print(MESSAGES[1], MESSAGES[4])

    if re.match('^((?![#$%]).)*$', user_password_inp):
        print(MESSAGES[1], MESSAGES[5])

    if re.match('^.{,5}$', user_password_inp):
        print(MESSAGES[6])

    if re.match('^.{17,}$', user_password_inp):
        print(MESSAGES[7])





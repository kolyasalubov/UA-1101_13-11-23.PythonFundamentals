import re

txt = input('Enter the password: ')

if 6 <= len(txt) <= 16 and re.search('[a-z]' and '[A-Z]' and '[0-9]' and '[@#$]', txt):
    print('Good job!')
else:
    print('Try again')

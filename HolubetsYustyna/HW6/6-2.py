"""Login while loop.
'First' >> greeting
different >> error message
"""

while True:
    if input('\u001b[0mPlease log in: ') == 'First':
        print('\u001b[35;1mSuccessful login. Welcome!\u001b[0m')
        break
    else:
        match input('\u001b[31;1mIncorrect login. Press Enter to try again or X > Enter to exit. \u001b[0m'):
            case '':
                 continue
            case 'X':
                break

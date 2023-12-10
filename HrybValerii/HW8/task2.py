import re


def is_valid_password(password: str, max_len=16, min_len=6) -> str:
    """The function takes a str-type argument and checks whether it is a valid password
    (contains 1 lower/upper case character, digit, 1 special character).
    A desired password length also can be specified with optional arguments.
    """

    patterns = {r'[a-z]': 'lower case letter', 
                r'[A-Z]': 'upper case letter', 
                r'\d': 'digit', 
                r'[$#@]': 'special character($#@)'}
    
    for pattern in patterns:
        if re.search(pattern, password) is None:
            return f'Password should contain at least one {patterns[pattern]}'
        continue
    
    if max_len >= len(password) >= min_len:
        return 'Password is valid'
    
    return f'Password length should be at least {min_len} and up to {max_len} characters'


if __name__ == '__main__':
    entered_password = input('Enter the password: ')
    print(is_valid_password(entered_password))

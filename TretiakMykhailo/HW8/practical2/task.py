import re


def validate_password(password: str):
    """Returns the password validity result"""
    return re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[S#@!$%^&*()_-]).{6,16}$', password) is not None


def main():
    passwords = ["123", "123456789101112", "Hello32&Za", "Az1^0", "$4Fd156frycd"]
    for password in passwords:
        print(f'Result of {password}: {validate_password(password)}')


if __name__ == '__main__':
    main()

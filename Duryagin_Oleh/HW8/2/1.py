import re


def check(password: str):
    """Returns the password validity result"""
    if 6 <= len(password) <= 16:
        return re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[S#@!$%^&*()_-]).{6,16}$", password) is not None
    return "Password length should be at least >5 and <17"


def main():
    password = input("Input password to check it: ")
    print(f'Result {check(password)}')


if __name__ == '__main__':
    main()

# Write a script that checks the login
def login_funk(login_name: str) -> bool:
    return True if login_name.capitalize() == "First" else False


while login_funk(input("Enter login:")) != 1:
    print("Wrong login name")
print("Greet")

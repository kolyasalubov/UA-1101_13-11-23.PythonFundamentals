def check_login():
    while True:
        user_login = input("Enter your login: ")

        if user_login.lower() == "first":
            print("Hello, welcome back!")
            break
        else:
            print("Error: Incorrect login. Please try again.")

if __name__ == "__main__":
    print("Welcome to the Login Checker!")

    # Call the function to check login
    check_login()
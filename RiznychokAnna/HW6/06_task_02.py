while True:
    user_login = input("Enter your login: ")
    
    if user_login == "First":
        print("Hello, user!")
        break 
    else:
        print("Error: Incorrect login. Please try again.")

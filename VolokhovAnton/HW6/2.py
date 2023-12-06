while True:
    login = input("Enter your login: ")
    
    if login == "First":
        print("Hello! Greetings, user!")
        break  # Exit the loop if the login is "First"
    else:
        print("Error: Invalid login. Please try again.")

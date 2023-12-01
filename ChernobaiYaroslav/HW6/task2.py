###############
# Solution №1 - in this scenario we can't access the result of user's input, but the code is less
###############

# while input("Enter your login: ") != "First":
#     print("Error! Wrong login, try again.")
# else:
#     print("Hello!")



###############
# Solution №2
###############

userInput = input("Enter your login: ")
i = True
while i:
    if userInput == "First":
        print(f"Hello, {userInput}!")
        i = False
    else:
        print("Error! Wrong login, try again.")
        userInput = input("Enter your login: ")
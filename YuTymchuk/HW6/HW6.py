############ Task 1 ###########
cheet_sheet = {"divisible by 2": [], "divisible by 3": [], "not divisible by 2 and 3": []}
for i in range(1, 11):
    if i % 2 == 0:
        cheet_sheet["divisible by 2"].append(i)
    if i % 3 == 0:
        cheet_sheet["divisible by 3"].append(i)
    if i % 2 != 0 and i % 3 != 0:
        cheet_sheet["not divisible by 2 and 3"].append(i)
print(cheet_sheet)

############ Task 2 ###########
LOGIN = "First"
user_login=(input("Please enter login: "))
while user_login!=LOGIN:
    user_login=(input("Sorry, this is invalid login. Please try again: "))
print(f"Glad to see you again, {user_login}! How are you today?")
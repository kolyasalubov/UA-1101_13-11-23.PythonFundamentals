# dict_login = {"login" : "First"}
# right_answer = False
# login = input("please Write a login:\n")
# while right_answer == False:
#     if login != dict_login["login"]:
#         login = input("Sorry thats a wrong login, please write another one:\n")
#     else:
#         print(f"Congraduations! your login {login} is correct.")
#         right_answer = dict_login["login"] == login

dict_login = {"login" : "First"}
right_answer = False
login = input("please Write a login:\n")
while login != dict_login["login"]:
    login = input("Sorry thats a wrong login, please write another one:\n")
print(f"Congraduations! your login {login} is correct.")
        


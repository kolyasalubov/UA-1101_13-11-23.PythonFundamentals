user_name = input ("Please, enter you name: ")
user_login = ""

while user_login != "First":
  user_login = input ("Please, enter your login: ")
  if user_login == "First":
    print (f"Hello, ", user_name)
  else:
    print ("Incorrect login!")
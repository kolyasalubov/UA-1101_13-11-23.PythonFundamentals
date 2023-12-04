i = 0
while i < 1:

    entered_login = [str(x) for x in input().split()]
    print(entered_login)
    if entered_login[0] == "first":
        print("Greetings!")
        break
    else:
        print("Error, wrong login!")

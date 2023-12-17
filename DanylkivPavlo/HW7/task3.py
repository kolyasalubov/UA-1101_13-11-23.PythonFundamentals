def calculator_of_characters(characters):
    user_dict = {}
    for i in characters:
        user_dict[i] = characters.count(i)
    return user_dict



user = input("Enter your word: ")
calculator_of_characters(user)
print(calculator_of_characters(user.replace(" ", "")))
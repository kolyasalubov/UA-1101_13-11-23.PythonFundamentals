def calculator_characters(characters):
    user_dict = {}
    for i in characters:
        user_dict[i] = characters.count(i)
    return user_dict



user = input("Enter your wordjr sentence: ")
calculator_characters(user)
print(calculator_characters(user.replace(" ", "")))
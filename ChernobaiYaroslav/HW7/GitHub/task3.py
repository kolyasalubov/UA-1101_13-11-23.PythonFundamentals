def calculate_characters(word: str)->dict:
    """
    Calculates the number of characters in a given string.
    Returns a dictionary consisting of a character and number of it's occurances.
    """
    temporary_dict = {}
    for i in word: #remove repeats
        if i in temporary_dict:
            continue
        temporary_dict[i] = word.count(i)
    return temporary_dict

user_input = input("Enter your sentence or a single word: ")
print(calculate_characters(user_input.replace(" ", "")))
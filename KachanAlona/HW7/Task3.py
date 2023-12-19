def number_of_characters(input_string: str):
    """
    Function that calculates the number of characters included in given string
    """
    tmp_set = set(input_string)
    number_of_characters_dict = {}
    for character in tmp_set:
        number_of_characters_dict[character] = input_string.count(character)
    return number_of_characters_dict

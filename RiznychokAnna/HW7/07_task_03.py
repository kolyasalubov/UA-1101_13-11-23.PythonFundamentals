def count_of_character(input_string) -> dict:
    """
    Clculates the number of characters

    :parameter: amount of character
    :return: number and characters
    :type: dictionary
    """
    char_count = {}

    for n in input_string:
        char_count[n] = input_string.count(n)
    # for n in input_string:
       
    #     if n in char_count:
    #         char_count[n]+= 1
    #     else:
    #         char_count[n]= 1
    return char_count
print(count_of_character("Chrismas"))

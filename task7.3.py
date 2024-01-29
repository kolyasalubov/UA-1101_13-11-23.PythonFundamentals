def calculate_character_counts(input_string):
    """
    This function takes a string as input and returns a dictionary with
    the count of each character in the string.

    Parameters:
    - input_string (str): Input string.

    Returns:
    - dict: A dictionary containing character counts.
    """
    char_counts = {}
    for char in input_string:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

result = calculate_character_counts("hello")
print("Character counts:", result)

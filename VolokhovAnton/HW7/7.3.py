def count_characters(input_string):
    """
    Counts the number of characters in a given string.

    Args:
    input_string (str): Input string to count characters.

    Returns:
    dict: A dictionary containing characters as keys and their respective counts as values.
    """
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def main():
    input_string = input("Enter a string: ")
    result = count_characters(input_string)
    print(result)

if __name__ == "__main__":
    main()

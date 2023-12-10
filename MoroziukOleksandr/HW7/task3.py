def count_characters(input_string):
    """
    Count the occurrences of each character in the given string.

    Parameters:
    - input_string (str): The input string for character counting.

    Returns:
    dict: A dictionary where keys are characters and values are their counts in the input string.
    """
    char_count = {}
    
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    
    return char_count

# Test block:
# input_str1 = "hello"
# output1 = count_characters(input_str1)
# print(output1)

# input_str2 = "SoftServe is't Super  "
# output2 = count_characters(input_str2)
# print(output2)
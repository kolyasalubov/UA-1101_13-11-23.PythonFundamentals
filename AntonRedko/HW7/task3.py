def count_string():
    string_to_count = input("Enter string: ")
    lower_case_of_string = string_to_count.lower()
    char_count = {char: lower_case_of_string.count(
        char) for char in lower_case_of_string}
    print(char_count)


"""
That function calculates the number
of characters included in given string
"""

count_string()

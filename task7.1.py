def find_largest_number(num1, num2):
    """
    This function takes two numbers as input and returns the largest one.

    Parameters:
    - num1 (float or int): First number.
    - num2 (float or int): Second number.

    Returns:
    - float or int: The largest number.
    """
    return max(num1, num2)

result = find_largest_number(8, 5)
print("The largest number is:", result)

def largest_of_two_numbers(num_1:int, num_2:int):
    """
    :int num_1:
    :int num_2:
    :return: the largest number between num1 and num2
    """
    if num_1 > num_2:
        return num_1
    elif num_1 < num_2:
        return num_2
    else:
        return f'{num_1} and {num_2} is equal.'

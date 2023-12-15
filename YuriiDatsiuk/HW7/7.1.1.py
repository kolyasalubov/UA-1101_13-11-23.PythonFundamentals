def largest_number(num1, num2):
    """
    return largest number of 2 numbers
    """
    return num1 if num1 >= num2 else num2

result = largest_number(3, 2)
print(f'the largest number is: ', result)

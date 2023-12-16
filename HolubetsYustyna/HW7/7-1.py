# Write a function that returns the largest number of two numbers

def max_two(num1, num2) -> float:
    """returns the largest number of 2 numbers"""
    return num1 if num1 > num2 else num2


num_in_1, num_in_2 = float(input('Enter a number: ')), float(input('Enter a number: ')) 

print(f'{max_two(num_in_1, num_in_2)} is the largest among {num_in_1, num_in_2}')
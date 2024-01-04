num1 = float(input('Enter number 1: '))
num2 = float(input('Enter number 2: '))


def largest_of_two_numbers(x, y):
    """Compare two numbers and show largest"""
    if x > y:
        return x
    elif x == y:
        return None
    return y


print(largest_of_two_numbers(num1, num2))
print("Docstring:", largest_of_two_numbers.__doc__)
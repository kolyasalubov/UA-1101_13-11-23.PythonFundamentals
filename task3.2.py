def manipulate_number(number):

    product = 1
    for digit in str(number):
        product *= int(digit)

    reversed_number = int(str(number)[::-1])

    sorted_digits = sorted(str(number))
    sorted_number = int(''.join(sorted_digits))

    return product, reversed_number, sorted_number

user_input = input("Enter the number: ")

try:
    user_number = int(user_input)
    result = manipulate_number(user_number)
    print(result)
except ValueError:
    print("Invalid input. Please enter a valid number.")

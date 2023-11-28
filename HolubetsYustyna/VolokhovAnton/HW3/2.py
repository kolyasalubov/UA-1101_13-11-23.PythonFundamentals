def manipulate_number(number):
    # Find the product of the digits
    product = 1
    for digit in str(number):
        product *= int(digit)
    
    # Reverse the number
    reversed_number = int(str(number)[::-1])
    
    # Sort the digits in ascending order
    sorted_digits = sorted(str(number))
    sorted_number = int(''.join(sorted_digits))
    
    return product, reversed_number, sorted_number


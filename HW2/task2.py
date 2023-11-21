def main(number: int):
    product = 1
    for digit in str(number):
        product *= int(digit)

    return product, int(str(number)[::-1]), int(''.join(sorted(str(number))))



product, reversed_num, sorted_num = main(1234)
print(f"Product of digits: {product}")
print(f"Reversed number: {reversed_num}")
print(f"Sorted number: {sorted_num}")

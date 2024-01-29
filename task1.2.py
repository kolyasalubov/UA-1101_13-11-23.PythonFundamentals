num = 1234

product_of_digits = 1
for digit in str(num):
    product_of_digits *= int(digit)

reverse_order = int(str(num)[::-1])

ascending_order = int(''.join(sorted(str(num))))

print(f"Product of digits: {product_of_digits}")
print(f"Number in reverse order: {reverse_order}")
print(f"Digits in ascending order: {ascending_order}")

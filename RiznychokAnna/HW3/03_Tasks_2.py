# # -find the product of the digits of this number
number = 12345
number_str = str(number)
product = 1

for digit in number_str:
    product *= int(digit)

#product = product * int(digit)

print(f"Product of the digits: {product}")


# write the number in reverse order 
number = 12345
reverse_order = int(str(number)[::-1])

print(f"Number in reverse order: {reverse_order}")


# # - in ascending order, you need to sort the numbers included in the given number

number = 3287

ascending_order = int(''.join(sorted(str(number))))
print(f"Number in ascending order: {ascending_order}")
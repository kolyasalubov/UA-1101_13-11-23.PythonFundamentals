# Finding the product of digits of a given number
number = 5008
product = 1

while number != 0:
      digit = number % 10
      product *= digit
      number //= 10

print("Product of digits of a number:", product)


# Write the number in reverse order:
number = 3789
reverse_number = int(str(number)[::-1])
print("The number in reverse order:", reverse_number)


# Sort numbers in ascending order
number = 7567
sorted_number = int(''.join(sorted(str(number))))
print("Sorted numbers in ascending order:", sorted_number)

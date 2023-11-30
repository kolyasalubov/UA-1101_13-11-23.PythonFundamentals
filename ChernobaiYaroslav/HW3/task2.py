number = input("Enter a four-digit natural number: ")

product = int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])

# Alternative solution:

# product = 1
# i = 0

# while i < len(number):
#     product *= int(number[i])
#     i += 1

print(f"The product of the digits of {number} is: ", product)

print(f"{number} in reversed order: ", number[::-1])

print(f"{number} sorted in ascending order: ", sorted(number))


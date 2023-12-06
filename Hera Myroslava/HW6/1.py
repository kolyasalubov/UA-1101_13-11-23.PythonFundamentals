even_numbers = [item for item in range(1, 11) if item % 2 == 0]

odd_numbers = [item for item in range(1, 11) if item % 2 == 1 and item % 3 == 0]

other_numbers = [item for item in range(1, 11) if item % 2 != 0 and item % 3 != 0]

print("Even numbers divisible by 2: ", even_numbers)
print("Odd numbers divisible by 3: ", odd_numbers)
print("Numbers not divisible by 2 and 3: ", other_numbers)
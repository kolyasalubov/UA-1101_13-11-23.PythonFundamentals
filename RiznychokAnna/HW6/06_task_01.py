num1 = [num for num in range(1, 11) if num % 2 == 0]
num2 = [num for num in range(1, 11) if num % 2 != 0 and num % 3 == 0]
num3 = [num for num in range(1, 11) if num % 2 != 0 and num % 3 != 0]

print("Even numbers divisible by 2:", num1)
print("Odd numbers divisible by 3:", num2)
print("Numbers not divisible by 2 and 3:", num3)

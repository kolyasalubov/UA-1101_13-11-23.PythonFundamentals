number1 = [number for number in range(1, 10) if number % 2 == 0]
number2 = [number for number in range(1, 10) if number % 2 != 0 and number % 3 == 0]
number3 = [number for number in range(1, 10) if number % 2 != 0 and number % 3 != 0]

print("Even numbers divisible by 2:", number1)
print("Odd numbers divisible by 3:", number2)
print("Numbers not divisible by 2 and 3:", number3)





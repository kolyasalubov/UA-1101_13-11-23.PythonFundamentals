number = int(input("Enter your number to calculate the factorial:"))
factorial = 1
for i in range(1, number + 1):
    factorial *= i

print(f'The factorial of {number} is {factorial}' if number >= 0 else f'The factorial of {number} is not defined')


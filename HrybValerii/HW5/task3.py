num = int(input("Enter the number whose factorial you want to calculate: "))
factorial = 1
for i in range(2, num + 1):
    factorial *= i

print(f'The factorial of {num} is {factorial}' if num >= 0 else f'The factorial of {num} is not defined')
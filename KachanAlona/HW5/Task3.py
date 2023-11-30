n = int(input("Enter number: "))

result = 1
for i in range(1, n+1):
    result *= i

print(f'Factorial of the {n}! = {result}')

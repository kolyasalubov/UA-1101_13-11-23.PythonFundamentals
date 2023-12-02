number = int(input("Enter the number you want to find a factorial of: "))
factorialNumber = 1

for i in range(1, number + 1):
    factorialNumber *= i

print(f"The factorial of the number {number} is {factorialNumber}")
# Write a script that will calculate the factorial of the entered

def factorial(number):
    if not isinstance(number, int):
        return "The number must be integer"
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact


numb = int(input('Enter the number you want to find the factorial of: '))

print(factorial(numb))

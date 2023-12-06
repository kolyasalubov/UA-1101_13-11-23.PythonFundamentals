def factorial(number):
    result = 1
    for num in range(1, number+1):
        result*=num
    return result

n = int(input("Enter a number to calculate its factorial: "))
res = factorial(n)
print(f"The factorial of {n} is: {res}")
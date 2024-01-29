def calculate_factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

user_input = int(input("Enter a number to calculate its factorial: "))
factorial_result = calculate_factorial(user_input)
print(f"{user_input}! =", factorial_result)

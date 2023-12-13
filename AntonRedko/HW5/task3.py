factorial_of_that_number = int(input("Enter number for a factorial: "))

factorial_result = 1
i = 1
if factorial_of_that_number > 0:
    while i <= factorial_of_that_number:
        factorial_result *= i
        i += 1
    print(f"Factorial {factorial_of_that_number} is {factorial_result}")
else:
    print("Factorial for negative number undefined!")

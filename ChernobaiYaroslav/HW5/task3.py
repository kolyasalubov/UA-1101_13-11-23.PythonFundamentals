number = int(input("Enter the number you want to find a factorial of: "))#add fact for 0 and 1
factorialNumber = 1

if number == 0 or number == 1:
    print(f"The factorial of the number {number} is {factorialNumber}")
elif number < 0:
    print("The factorial of a negative number doesn't exist!")
else:
    for i in range(1, number + 1):
        factorialNumber *= i

    print(f"The factorial of the number {number} is {factorialNumber}")
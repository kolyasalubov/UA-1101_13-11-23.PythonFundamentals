def fibonacci_sequence(n):
    # Initiate the first two numbers in the sequence
    a, b = 0, 1
    fibonacci_list = [a]  # Initialize the list with the first number (0)

    # Generate the sequence while the current number is less than or equal to 'n'
    while b <= n:
        fibonacci_list.append(b)

        # Calculate the next Fibonacci number
        a, b = b, a + b

    return fibonacci_list

# Taking input from the user for the upper limit 'n'
user_input = int(input("Enter a number: "))
result = fibonacci_sequence(user_input)
print(result)

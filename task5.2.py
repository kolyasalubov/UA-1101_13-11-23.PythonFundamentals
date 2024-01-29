def fibonacci_sequence(n):
    fib_sequence = [0, 1]

    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    print("Fibonacci Sequence up to", n, ":", fib_sequence)

user_input = int(input("Enter a number to generate Fibonacci sequence up to: "))
fibonacci_sequence(user_input)

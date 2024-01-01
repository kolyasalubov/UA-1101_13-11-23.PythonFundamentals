def print_fibonacci(n):
    fib_list = []
    a, b = 0, 1

    while a <= n:
        fib_list.append(a)
        a, b = b, a + b

    print("Fibonacci numbers up to", n, ":", fib_list)

max_number = int(input("Enter the maximum number for Fibonacci sequence: "))

print_fibonacci(max_number)

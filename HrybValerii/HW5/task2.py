n = float(input("Enter the n number (generates Fibonacci series up to n): "))

if n < 0:
    print("Entered number is negative, whereas Fibonacci series starts at 0")
elif n == 0:
    print(f'Fibonacci series up to {n} is {0}')
else:
    fib_series = [0, 1]
    while fib_series[-1] + fib_series[-2] <= n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    print(f'Fibonacci series up to {n} is', *fib_series)






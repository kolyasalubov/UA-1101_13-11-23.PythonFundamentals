# Print Fibonacci numbers up to the entered number n, using cycles.
def fib(number: int) -> int:
    if number < 0:
        print("Incorrect number, must be >0")
    else:
        return number if number <= 1 else fib(number - 1) + fib(number - 2)


input_number = int(input('Enter the number to fide Fibonacci numbers: '))

print([fib(n) for n in range(input_number)])

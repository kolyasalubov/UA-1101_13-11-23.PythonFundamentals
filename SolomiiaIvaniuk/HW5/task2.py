fibonacci_till_to = int(input("Enter number, Fibonacci numbers up to: "))
i = 1
fibonacci_numbers = [0, 1]
while i <= fibonacci_till_to:
    fibonacci_numbers.append(fibonacci_numbers[i] + fibonacci_numbers[i-1])
    i += 1

print(fibonacci_numbers)


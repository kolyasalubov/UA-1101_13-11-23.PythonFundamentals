fibonacciNumbers = [0, 1]

upperLimit = int(input("Enter an upper limit for Fibonacci sequence: "))

i = 1

while i < len(fibonacciNumbers):
    if fibonacciNumbers[i] + fibonacciNumbers[i - 1] <= upperLimit:
        fibonacciNumbers.append(fibonacciNumbers[i] + fibonacciNumbers[i - 1])
        i += 1
    else: 
        break

print("Your Fibonacci sequence is:", ', '.join(map(str, fibonacciNumbers)))
elements_count = int(input('Enter lenght Fibonacci numbers '))

i = -1
sym1 = 0
sym2 = 1

fibonacci_numbers = [sym1, sym2]

while i <= elements_count:
    i += 1

    if i < 3:
        continue
    number = sym1 + sym2
    fibonacci_numbers.append(number)

    sym1 = sym2
    sym2 = number

print(fibonacci_numbers)
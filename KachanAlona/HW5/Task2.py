n = int(input("Enter number: "))

first = 0
second = 1
print(first, end=', ')
next_number = 1
while next_number < n:
    print(next_number, end=', ')
    next_number = first + second
    first = second
    second = next_number

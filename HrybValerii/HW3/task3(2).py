from functools import reduce

#product of all digits
number = input("Enter the number: ")
digits = [int(i) for i in list(number)]
product1 = reduce(lambda a, b: a * b, digits)
print(product1)

#alternative solution
def digit_prod(n):
    if n < 10:
        return n
    else:
        return (n % 10) * digit_prod(n // 10)


product2 = digit_prod(int(number))
print(product2)


#number in reversed order
print(number[::-1])


#digits sorted in ascending order
print(*sorted(digits))
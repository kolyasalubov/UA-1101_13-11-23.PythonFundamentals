a = int(input('a = '))
b = int(input('b = '))

print(f'Original values: a = {a}, b = {b}')

a, b = b, a

print(f'Swapped values: a = {a}, b = {b}')

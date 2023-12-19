even = []
odd = []
no_divisible = []
for x in range(1, 11):
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
    if x % 2 != 0 and x % 3 != 0:
        no_divisible.append(x)

print(f'List of even elements: {even}')
print(f'List of odd elements: {odd}')
print(f'List of elements that are not divisible by 2 and 3: {no_divisible}')
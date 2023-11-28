# four-digit natural number: product/ reverse/ ascending

n = int(input('write a four-digit natural number: '))

n1 = []

for i in range (1,5):
    n1.append(n % 10)
    n = n // 10

prod_n = 1
n_rev = ''

for i in n1:
    prod_n *= i
    n_rev += str(i)

for j in range(0, len(n1) - 1):
    for i in range(0, len(n1) - 1 - j):
        if n1[i] > n1[i + 1]:
            t = n1[i]
            n1[i] = n1[i + 1]
            n1[i + 1] = t

# or n1.sort()

new_line = '\n'
print(f'{new_line}product of the digits: {prod_n}{new_line}reverse order: {n_rev}{new_line}ascending order: {n1}')
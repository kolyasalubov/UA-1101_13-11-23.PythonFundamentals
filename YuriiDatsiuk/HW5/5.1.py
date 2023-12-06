elements_counts = int(input('Enter counts of elements '))

elements_list = list(range(1, elements_counts + 1))

print(elements_list)

for i in elements_list:
    element_float = float(i)
    print(element_float, end=' ')
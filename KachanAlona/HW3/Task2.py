four_digit_number = 5038
print(f'Original number is: {four_digit_number}')

list_of_str = list(str(four_digit_number))
list_of_int = []
for elem in range(4):
    list_of_int.append(int(list_of_str[elem]))

product_of_digit = 1
for num in list_of_int:
    product_of_digit *= num
print(f'Product of the digits of this number: {product_of_digit}')

reverse_of_number = ''.join(list_of_str[::-1])
print(f'Number in reverse order: {reverse_of_number}')

# ascending_order = []
for num in range(4):
    for j in range(0, 3-num):
        if list_of_int[j] > list_of_int[j + 1]:
            list_of_int[j], list_of_int[j + 1] = list_of_int[j + 1], list_of_int[j]

print(f'Ascending order of digits: {" ".join(map(str, list_of_int))}')

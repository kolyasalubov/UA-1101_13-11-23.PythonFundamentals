even_num_divisible_2 = []

for num in range(1,11):
    if num % 2 == 0:
        even_num_divisible_2.append(num)
print(even_num_divisible_2)



odd_num_divisible_3 = []

for num in range(1,11):
    if num % 3 == 0:
        odd_num_divisible_3.append(num)
print(odd_num_divisible_3)



num_divisible_2_3 = []

for num in range(1, 11):
    if num % 2 != 0 and num % 3 != 0:
        num_divisible_2_3.append(num)
print(num_divisible_2_3)





even_num_dis_2 = []
odd_num_dis_3 = []
not_equal_two_digit = []

for i in range(1,11):
    if i % 2 ==0:
        even_num_dis_2.append(i)
print(even_num_dis_2,end=" ")

for j in range(1,11):
    if j % 3 == 0:
        odd_num_dis_3.append(j)
print(odd_num_dis_3, end=" ")

for n in range(1,11):
    if n % 2 and n % 3 != 0:
        not_equal_two_digit.append(n)
print(not_equal_two_digit,end=" ")
print('Even numbers in the range from 1 to 10 that are divisible by 2:')
for i in range(1, 11):
    if i % 2 == 0:
        print(i, end=' ')


print('\n\nOdd numbers in the range from 1 to 10 that are divisible by 3:')
list_of_odd_numbers = [print(i, end=' ') for i in range(1, 11) if i % 3 == 0 and i % 2 != 0]


print('\n\nNumbers in the range from 1 to 10 that are not divisible by 2 and 3:')
counter_for_range_10 = 0
while counter_for_range_10 < 10:
    if counter_for_range_10 % 2 != 0 and counter_for_range_10 % 3 != 0:
        print(counter_for_range_10, end=' ')
    counter_for_range_10 += 1

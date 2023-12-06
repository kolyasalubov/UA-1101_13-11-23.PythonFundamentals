list_even_div_2 = [i for i in range(1, 11) if i%2 == 0 ]
list_odd_div_3  = [i for i in range(1, 11) if i%2 != 0 and i%3 == 0]
list_notdiv_2_3 = [i for i in range(1, 11) if i%2 != 0 and i%3 != 0]

print('numbers that is even and divide by 2: ', list_even_div_2)
print('numbers that is odd and divide by 3: ', list_odd_div_3)
print('numbers that is not divide by 2 and 3: ', list_notdiv_2_3)
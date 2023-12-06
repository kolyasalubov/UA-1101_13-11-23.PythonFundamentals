""" in range(1, 10) determine 
even numbers divisible by 2
odd numbers divisible by 3
numbers not divisible by 2 and 3 """

num_10 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

div_2, div_3, div_23 = set(), set(), set()

for num in num_10:
    if not num % 2:
        div_2.add(num)
    elif not num % 3:
        div_3.add(num)
    if num % 2 and num % 3: 
        div_23.add(num)

print('\nEven nums divisible by 2: {}\nOdd nums divisible by 3:  {}\n\
Not divisible by 2 and 3: {}\n'.format(div_2, sorted(div_3), div_23))


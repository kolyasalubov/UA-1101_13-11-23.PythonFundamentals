list_even_div_2 = []
list_odd_div_3 = []
list_notdiv_2_3 = []

for i in range(1, 11):
  if i%2 == 0:
   list_even_div_2.append(i)
  if i%3 == 0:
   list_odd_div_3.append(i)
  if i%2 != 0 or i%3 != 0:
   list_notdiv_2_3.append(i)

print(list_even_div_2)
print(list_odd_div_3)
print(list_notdiv_2_3)
# Divided numbers in range from 1 to 10
def divide_(lst_1: list):
    return f"Even numbers that are divide by 2 {[numb for numb in lst_1 if numb % 2 == 0]}\n" \
           f"Odd numbers that are divide by 3 {[numb for numb in lst_1 if numb % 3 == 0]}\n" \
           f"Other numbers that are not divide by 2 and 3 {[numb for numb in lst_1 if numb % 2 == 1 and numb % 3 == 1]}"


lst = list(range(1, 11))
print(divide_(lst))


## in order of priority
# for numb in lst:
#     var = divmod(numb, 2)
#     var2 = divmod(numb, 3)
#     if var[1] == 0:
#         print(f"{numb} Even")
#     elif var2[1] == 0:
#         print(f"{numb} Odd")
#     else:
#         print(f"{numb} not in %3 and %2 = Other")

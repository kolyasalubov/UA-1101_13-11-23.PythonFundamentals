#Program realization using for loop and list comprehension
even_div_by_2 = [num for num in range(1, 11) if num % 2 == 0]  # Even numbers divisible by 2
odd_div_by_3 = [num for num in range(1, 11) if num % 2 != 0 and num % 3 == 0]  # Odd numbers divisible by 3
not_div_by_2_3 = [num for num in range(1, 11) if num % 2 != 0 and num % 3 != 0]  # Numbers not divisible by 2 and 3

print("Even numbers divisible by 2:", even_div_by_2)
print("Odd numbers divisible by 3:", odd_div_by_3)
print("Numbers not divisible by 2 and 3:", not_div_by_2_3)



# Progran realization using for loop and match case 
# def sort_numbers():
#     for num in range(1, 11):
#         match num:
#             case even if num % 2 == 0:
#                 print(f"{num} is even and divisible by 2")
#             case odd if num % 2 != 0 and num % 3 == 0:
#                 print(f"{num} is odd and divisible by 3")
#             case not_divisible if num % 2 != 0 and num % 3 != 0:
#                 print(f"{num} is not divisible by 2 and 3")
# sort_numbers()
import random

numbers = int(input("Enter the number of elements: "))

int_list = [random.randint(0, 100) for _ in range(numbers)]
float_list = [float(element) for element in int_list]

print("Original list:", int_list)
print("Float list:", float_list)
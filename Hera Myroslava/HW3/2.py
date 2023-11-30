number = input("Enter a four-digit natural number: ")

if len(number) != 4 or not number.isdigit():
    print("Error!")
else:
    number = int(number)

product = 1
for temp_number in str (number):
   product *= int(temp_number)
print(f"Product of digits {product}")

number_reversed = int(str(number)[::-1])
print(f"Reversed number: {number_reversed}")

digits_sorted = sorted(str(number))
number_sorted = int (''.join(digits_sorted))
print(f"Sorted number: {number_sorted}")
four_digit_number = 1245

first_digit = int(str(four_digit_number)[1])
second_digit = int(str(four_digit_number)[2])
third_digit = int(str(four_digit_number)[4])
forth_digit = int(str(four_digit_number)[5])
product_digits = first_digit * second_digit * third_digit * forth_digit
reverse_order = str(four_digit_number)[::-1]

switch_to_string=list(str(four_digit_number))
ascending_order = ''.join(sorted (switch_to_string))
  

print(f"Product of digits is: {40}, reverse order - {5421}, ascending order -{1245}")

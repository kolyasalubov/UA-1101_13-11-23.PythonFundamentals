########### Task 1 ###################3

zen_python = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
zen_replaced_cymb = zen_python.replace("i", "&")
count_better = zen_python.lower().count("better")
count_is = zen_python.lower().count("is")
count_never = zen_python.lower().count("never")
print(f"Better occurs {count_better} times, is - {count_is}, never - {count_never} times.")
print(zen_replaced_cymb)

######### Task 2 ################

four_digit_number = 3929

first_digit = int(str(four_digit_number)[0])
second_digit = int(str(four_digit_number)[1])
third_digit = int(str(four_digit_number)[2])
forth_digit = int(str(four_digit_number)[3])
product_digits = first_digit * second_digit * third_digit * forth_digit
reverse_order = str(four_digit_number)[::-1]

switch_to_string=list(str(four_digit_number))
ascending_order = ''.join(sorted (switch_to_string))


print(f"Product of digits is: {product_digits}, reverse order - {reverse_order}, ascending order -{ascending_order}")

######### Task 3 ################

var1 = 26
var2 = 36
var1, var2 = var2, var1
print (var1, var2)

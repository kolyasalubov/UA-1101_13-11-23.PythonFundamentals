#### PYTHON'S PHYLOSOPHY(TASK 1) ####

zen_of_python = '''Beautiful is better than ugly.
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
Namespaces are one honking great idea -- let's do more of those!'''

word_to_find = ['better', 'never', 'is']
counter = []
i = 0
while i < len(word_to_find):
    counter = zen_of_python.count(word_to_find[i])
    print(f"The word '{word_to_find[i]}' appears '{counter}' times")
    i += 1

edited_zen = str(zen_of_python).replace('i', '&')


print(edited_zen.upper())


#### FOUR-DIGIT NUMBER(TASK 2) ####

number = 3476231
product = 1
for each_elem in str(number):
    product *= int(each_elem)

reversed_number = str(number)[::-1]

sorted_number = int("".join(sorted(str(number))))

print(sorted_number)
print(int(reversed_number))
print(product)

#### INTERCHANGE(TASK 3) ####

variable_one = 'string'
variable_two = 12

variable_one, variable_two = variable_two, variable_one

print(variable_one, variable_two)

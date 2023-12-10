philosophy  = """

The Zen of Python, by Tim Peters   

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
Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

occurrences_better = philosophy.lower().count("better")
occurrences_never = philosophy.lower().count("never")
occurrences_is = philosophy.lower().count("is")


print(f'The number of occurrences with "better": {occurrences_better}')
print(f'The number of occurrences with "never": {occurrences_never}')
print(f'The number of occurrences with "is": {occurrences_is}')




# In this case all letters are in uppercase
all_letters_in_upper_case = philosophy.upper()
print (all_letters_in_upper_case.upper())


# - replace all occurrences of the symbol “i” with “&”

result = philosophy.replace("i", "&")
print(result)

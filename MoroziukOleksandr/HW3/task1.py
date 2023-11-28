python_philosophy = """
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

# Task 1: Count occurrences of words
occurrences_better = python_philosophy.lower().count("better")
occurrences_never = python_philosophy.lower().count("never")
occurrences_is = python_philosophy.lower().count("is")

print(f'Number of occurrences of "better": {occurrences_better}')
print(f'Number of occurrences of "never": {occurrences_never}')
print(f'Number of occurrences of "is": {occurrences_is}')

# Task 2: Display all text in uppercase
uppercase_text = python_philosophy.upper()
print("\nUppercase Text:")
print(uppercase_text)

# Task 3: Replace all occurrences of the symbol "i" with "&"
replace_i_with_ampersand = python_philosophy.replace('i', '&')
print("\nText with 'i' replaced by '&':")
print(replace_i_with_ampersand)

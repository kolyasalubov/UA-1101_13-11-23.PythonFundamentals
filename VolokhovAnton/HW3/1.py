philosophy = '''
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
'''

# Counts the occurence of  words "better", "never" and "is" among text
# Converts letters to lowercase in order to avoid miscalculations if the word starts with an uppercase letter

count_better = philosophy.lower().count("better")
count_never = philosophy.lower().count("never")
count_is = philosophy.lower().count("is")

# Converts all text to uppercase
philosophy_upper = philosophy.upper()

# Replaces "¡" with "&" and "I" with "&" to ensure correct performance if "I" is an uppercase letter
philosophy_replaced = philosophy.replace("i", "&").replace("I", "&")

print(f"Occurrences of 'better': {count_better}")
print(f"Occurrences of 'never': {count_never}")
print(f"Occurrences of 'is': {count_is}\n")
print(f"Uppercase Text:\n {philosophy_upper}")
print(f"Text with ¡ replaced by &:\n {philosophy_replaced}")

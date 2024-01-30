zen_of_python = """Beautiful is better than ugly.
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
Namespaces are one honking great idea -- let's do more of those!"""

separated_zen_by_line = zen_of_python.split('.')
print(' Number of occurences of the words:')
counter = 1
for line in separated_zen_by_line:
    print(f'Line {counter}: "better" - {line.count("better")} times,'
          f' "never" - {line.count("never")} times, "is" - {line.count("is")} times')
    counter += 1

print('\n Zen in uppercase:')
print(zen_of_python.upper())

print('\n Replaced "i":')
zen_replaced = zen_of_python.replace('i', '&')
print(zen_replaced)
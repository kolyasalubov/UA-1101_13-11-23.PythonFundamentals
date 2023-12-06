#import this
q = '''
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
countb = 0
countn = 0
counti = 0
x = q.split(" ")
print(x)
for i in x:
    if i in ["better"]:
        countb +=1
print("The number of word 'better' is: ",countb)
for i in x:
    if i in ["never"]:
        countn +=1
print("The number of word 'never' is: ",countn)
for i in x:
    if i in ["is"]:
        counti +=1
print("The number of word 'is' is: ",counti)

b = q.upper()
print(b)

modified_string_q = q.replace('i', '&')

print(modified_string_q)

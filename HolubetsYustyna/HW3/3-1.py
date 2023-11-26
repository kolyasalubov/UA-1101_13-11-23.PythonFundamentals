# Py Philosophy: better never is/ uppercase/ i >> &

zen = """
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
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""


def findAll(word):
  li = zen.split(word)
  return len(li) - 1

# or:
# zen.count('better') / zen.count('never') / zen.count('is')

# or:
# def findAll(word):
  zen_ch = zen
  count = 0
  while True:
    pos = zen_ch.find(word)
    if pos == -1:
      break
    if pos:
      count += 1
    zen_ch = zen_ch[pos + len(word):]
  return count


for w in ['better', 'never', 'is']:
   print(f'the word "{w}" occurs {findAll(w)} times')

print(zen.upper())
print(zen.replace('i', '&'))
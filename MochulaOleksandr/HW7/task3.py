
def count_char(word):
    number_char = {}
    for x in word:
        if x in number_char:
            number_char[x] += 1
        else:
            number_char[x] = 1
    return print(number_char)

count_char("hello")
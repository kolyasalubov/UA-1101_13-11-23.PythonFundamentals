txt = input('Enter some text: ')

def letter_counter(any_text):
    letters = []
    letters_dict = {}
    for x in any_text:
        letters.append(x)
        letters.append(letters.count(x))
    for i in range(0, len(letters), 2):
        letters_dict[letters[i]] = letters[i + 1]
    return letters_dict


print('My array: ', letter_counter(txt))


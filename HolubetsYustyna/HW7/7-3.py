# Write a function that calculates the number of characters included in a given string

def charNumber_1(str) -> dict:
    """returns the frequencies of characters in a string as dict {'char': freq} )"""
    return {key: str.count(key) for key in tuple(str)}


# def charNumber_2(str) -> dict:
#     """returns the frequencies of characters in a string as dict {'char': freq} )"""
#     freq_di = {}.fromkeys(tuple(str))
#     for keys in freq_di.keys():
#         freq_di[keys] = str.count(keys)
#     return freq_di


str_inp = input('Enter your string: ')

print(charNumber_1(str_inp))
# print(charNumber_2(str_inp))
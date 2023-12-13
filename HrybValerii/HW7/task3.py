def char_calculator(string: str) -> dict:
    '''
    Thefunction takes a string and returns a dictionary, where key are characters and numbers of those characters are values
    '''
    return {character: string.count(character) for character in set(string)}

# print(char_calculator('hello'))
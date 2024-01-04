def char_count(string: str) -> dict:
    return {char: string.count(char) for char in set(string)}

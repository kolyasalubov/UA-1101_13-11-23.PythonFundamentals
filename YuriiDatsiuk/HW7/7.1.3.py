def countletters(word: str) -> dict:
    """
    :return: dict with key - letter, value - count in word
    """
    result = {}
    for i in word:
        if result.get(i):
            continue

        result[i] = word.count(i)

    return result

print(countletters('helloooy'))
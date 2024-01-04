def count_sheeps(sheep):
    counter = 0
    for x in sheep:
        if x:
            counter += 1
    return counter
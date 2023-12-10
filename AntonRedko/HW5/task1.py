list_integer_type = [1, 2, 3, 4, 5, 6, 7, 'string', True]
i = 0
while i < len(list_integer_type):
    if isinstance(list_integer_type[i], bool):
        print(
            f"Element {list_integer_type[i]} have a boolean type, can't convert")
        i += 1
        continue
    elif isinstance(list_integer_type[i], int):
        list_integer_type[i] = float(list_integer_type[i])
        i += 1
    else:
        print(
            f"Element {list_integer_type[i]} isn't integer, can't convert to float type")
        i += 1
        continue


print(list_integer_type)

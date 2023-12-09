# Create a list that contains elements of integer type, then use the loop to change type to float
def transformList(list_1: list) -> list:
    return [float(x) for x in list_1]


lst = list(range(100))

print(transformList(lst))

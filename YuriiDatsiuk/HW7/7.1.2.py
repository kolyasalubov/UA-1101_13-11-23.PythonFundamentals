
def calculate_area_rectangle():
    length = float(input('length is '))
    width = float(input('width is '))

    return length * width
def calculate_area_triangle():
    side1 = float(input('side 1 is '))
    side2 = float(input('side 2 is '))
    return (1/2) * side1 * side2
def calculate_area_circle():
    radius = float(input('radius 1 is '))
    PI = 3.14
    return PI * radius ** 2
def calculate_area(user_object):
    """
    :param type of object (int):
    :return area (float):
    """

    result = 0
    match user_object:
        case '1':
            result = calculate_area_rectangle()
        case '2':
            result = calculate_area_triangle()
        case '3':
            result = calculate_area_circle()
        case _:
            print('choosen not correct object')

    return result

choise = input('choose the object to calculate the area: (1:rectangle, 2:triangle, 3:circle ')
result = calculate_area(choise)
print('area is ', result)



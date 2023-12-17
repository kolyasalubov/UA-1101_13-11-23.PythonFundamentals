import calcutate_area as ca
def calculate_area(user_object):
    """
    :param type of object (int):
    :return area (float):
    """

    result = 0
    match user_object:
        case '1':
            result = ca.calculate_area_rectangle()
        case '2':
            result = ca.calculate_area_triangle()
        case '3':
            result = ca.calculate_area_circle()
        case _:
            print('choosen not correct object')

    return result

choise = input('choose the object to calculate the area: (1:rectangle, 2:triangle, 3:circle ')
result = calculate_area(choise)
print('area is ', result)
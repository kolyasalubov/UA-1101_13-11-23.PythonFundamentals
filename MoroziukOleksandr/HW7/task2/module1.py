# module1.py

def calc_area_rectangle():
    """
    Calculate the area of a rectangle.

    Parameters:
    - side_a (float): Length of one side of the rectangle.
    - side_b (float): Length of the other side of the rectangle.

    Returns:
    float: The calculated area of the rectangle.
    """
    print('Enter the lengths of the sides of the rectangle: ')
    side_a = float(input('Side a: '))
    side_b = float(input('Side b: '))

    print(f'Area of a rectangle: ' + str(side_a*side_b))

    return side_a*side_b

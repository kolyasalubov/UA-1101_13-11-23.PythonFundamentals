# module3.py
import math

def calc_area_triangle_circle():
    """
    Calculate the area of a circle based on its radius.

    This function takes user input for the radius of a circle and
    calculates the area using the formula: area = 2 * pi * radius.

    Returns:
    float: The calculated area of the circle.
    """
    radius = float(input('Enter the radius of the circle: '))

    print(f'Area of the circle: {2*math.pi*radius}')

    return 2*math.pi*radius

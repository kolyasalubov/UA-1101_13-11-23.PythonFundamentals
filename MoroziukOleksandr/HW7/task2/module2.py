# module2.py
import math

# Area of Triangle Formula
def calc_area_triangle_height():
    """
    Calculate the area of a triangle using height and base lenght.

    Parameters:
    - base: Length of side a
    - height: Length of side b

    Returns:
    - area: Area of the triangle
    """
    base = float(input('Enter the length of the base of the triangle: '))
    height = float(input('Enter the height of the triangle: '))

    print(f'Area of a triangle: {str(0.5*base*height)}')

    return 0.5*base*height


# Area of Triangle Using Heron's Formula
def calc_area_triangle_Heron():
    """
    Calculate the area of a triangle using method Herona (when is known the length of the 3 sides of the triangle).

    Parameters:
    - side_a: Length of side a
    - side_b: Length of side b
    - side_c: Length of side c

    Returns:
    - area: Area of the triangle
    """
    side_a = float(input('Enter the length of the side a: '))
    side_b = float(input('Enter the length of the side b: '))
    side_c = float(input('Enter the length of the side c: '))

    print(f'Area of a triangle: {(side_a*side_b*side_c)/2}')

    return (side_a*side_b*side_c)/2


# Area of Triangle With 2 Sides and Included Angle (SAS)
def calculate_triangle_area_sas():
    """
    Calculate the area of a triangle using the Side-Angle-Side (SAS) method.

    Parameters:
    - side_a: Length of side a
    - side_b: Length of side b
    - angle_rad: Included angle in radians

    Returns:
    - area: Area of the triangle
    """
    side_a = float(input('Enter the length of the side a: '))
    side_b = float(input('Enter the length of the side b: '))
    angle_rad = float(input('Enter the angle value in radians: '))

    print(f'Area of a triangle: {0.5 * side_a * side_b * math.sin(angle_rad)}')

    return 


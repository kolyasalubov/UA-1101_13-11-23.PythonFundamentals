import math
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
    return math.pi * math.pow(radius, 2)




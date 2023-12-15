from math import pi


def TriangleArea():
    height = float(input("Enter height: "))
    base = float(input("Enter base: "))
    area_triangle = 1/2*height*base
    print(f"Area of triangle: {area_triangle}")
    return area_triangle


"""
Function TriangleArea calcucal triangle's area
based on it's parameters: base and height
"""


def RectangleArea():
    height = float(input("Enter height: "))
    length = float(input("Enter length: "))
    area_rectangle = height*length
    print(f"Area of rectangle: {area_rectangle}")
    return area_rectangle


"""
Function RectangleArea calcucal rectangle's area
based on it's parameters: base and height
"""


def CircleArea():
    radius = float(input("Enter radius: "))
    area_circle = pi*radius**2
    print(f"Area of circle: {area_circle}")
    return area_circle


"""
Function CircleArea calcucal circle's area
based on it's parameters: radius
"""

area_you_want = input("Enter area to count(Triangle, Rectangle, Circle): ")
lower_case_area = area_you_want.lower()

match lower_case_area:
    case "triangle":
        TriangleArea()
    case "rectangle":
        RectangleArea()
    case "circle":
        CircleArea()

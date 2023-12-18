from math import pow, pi


def rectangle_area(height, width):
    """calculate the area of rectangle"""
    return height * width


def triangle_area(base, height):
    """calculate the area of triangle"""
    return 0.5 * base * height


def circle_area(radius):
    """calculate the area of circle"""
    return pi * pow(radius, 2)

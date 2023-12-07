# Write a program that calculates the area of a rectangle, triangle and circle
# 3 functions depending on user's choice


from math import pi


def area_rectangle(length, width):
    """the area of rectangle: length * width"""
    return length * width


def area_triangle(base, height):
    """the area of triangle: 0.5 * base * height"""
    return 0.5 * base * height


def area_circle(radius):
    """the area of circle: PI * radius ** 2"""
    return pi * radius ** 2


inp_figure = input('Enter r, t or c depending on the figure (rectangle, triangle or circle): ')

match inp_figure:
    case 'r':
        print('The area of your rectangle =', area_rectangle(float(input('Enter width: ')), float(input('Enter height: '))))
    case 't':
        print('The area of your triangle =', area_triangle(float(input('Enter base: ')), float(input('Enter height: '))))
    case 'c':
        print('The area of your circle =', area_circle(float(input('Enter radius: '))))

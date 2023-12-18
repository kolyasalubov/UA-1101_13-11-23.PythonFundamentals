from math import pow, pi


def area_of_rectangle(a, b):
    return a * b


def area_of_triangle(h, a):
    area = 0.5 * h * a
    return round(area, 3)


def area_of_circle(radius):
    return pi * pow(radius, 2)

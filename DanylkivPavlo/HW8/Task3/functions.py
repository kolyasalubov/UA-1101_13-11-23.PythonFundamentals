from math import pi
from math import pow


def area_of_rectangle(numr1,numr2):
    """This function determines
    the area of the rectangle"""
    sumr = numr1 * numr2
    print("The area of the rectangle is: ", sumr)
    return sumr

def area_of_triangle(height,base):
    """This function determines
    the area of the triangle"""
    sumt = 0,5 * height * base
    print("The area of the triangle is :", sumt)
    return sumt

def area_of_circle(radius):
    """This function determines
        the area of the circle"""
    sumc = pi * pow(radius,2)
    print("The area of circle is: ", sumc)
    return sumc
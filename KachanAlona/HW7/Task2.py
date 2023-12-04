from math import sqrt, pi
# def area_calculates(type_of_figure, *args):
def area_of_rectangle(length, width):
    return length * width

def area_of_triangle(side_a, side_b, side_c):
    semi_perimetr = (side_a + side_b + side_c)/2
    area = sqrt(semi_perimetr * (semi_perimetr - side_a) *
                (semi_perimetr - side_b) * (semi_perimetr - side_c))
    return round(area, 3)

def area_of_circle(radius):
    return pi * radius ** 2

print(round(area_of_circle(30), 3))

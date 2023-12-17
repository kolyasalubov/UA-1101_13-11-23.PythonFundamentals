from math import pi

def rectangle_area():
    dimensions = list(input("Please enter length and width, separated comma: ").split(sep=","))
    res = int(dimensions[0]) * int(dimensions[1])
    print(f"The area of rectangle is {res}.")


def triangle_area():
    dimensions = list(input("Please enter base and high, separated comma: ").split(sep=","))
    res = int(dimensions[0]) * int(dimensions[1]) * 0.5
    print(f"The area of triangle is {res}.")


def circle_area():
    dimensions = input("Please enter radius: ")
    res = pow(int(dimensions),2) * pi
    print(f"The area of circle is {res}.")

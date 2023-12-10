def area_triangle(high,side):
    return (high * side)/2
"""This function returns area of triangle"""

def area_circle(radius):
    return 3.14*(radius**2)
"""this function returns area of circle"""

def area_rectangle(lenth,width):
    return lenth * width
"""this function returns area of rectangle"""


figure = input("Which figure you want to calculate the area?\n")

while True:
    if figure == "triangle":
        triangle_high = float(input("please write high\n"))
        triangle_side = float(input("please write side\n"))
        print(f"Area of a triangle is: {area_triangle(triangle_high,triangle_side)}")
        break

    elif figure == "circle":
        circle_radius = float(input("please write a radius\n"))
        print(f"Area of a circle is: {area_circle(circle_radius)}")
        break

    elif figure == "rectangle":
        rectangle_lenth = float(input("please write a lenth\n"))
        rectangle_width = float(input("please write a width\n"))
        print(f"Area of a rectangle is: {area_rectangle(rectangle_lenth,rectangle_width)}")
        break

    else:
        figure = input("Sorry you can choose only rectangle, circle and triangle\n")
import math

def rectangleArea(length, width):
    """Calculate the area of a rectangle using it's width and length."""
    return length * width

def triangleArea(base, height):
    """Calculate the area of a triangle using it's base and height."""
    return base * height / 2

def circleArea(radius):
    """Calculate the area of a circle using it's radius"""
    return round(math.pi * radius ** 2, 2)

print("Use the following numbers to choose a figure and calculate its area:\n\
1. Rectangle.\n2. Triangle\n3. Circle\n4. Exit ")
user_input = ""
while user_input != "4":
    user_input = input("Enter you choise: ")
    match user_input:
        case "1":
            rectangle_length = float(input("Enter the length of a rectangle: "))
            rectangle_width = float(input("Enter the length of a rectangle: "))
            print(f"The area of a rectangle is: {rectangleArea(rectangle_length, rectangle_width)}")
        case "2":
            triangle_base = float(input("Enter the base of a triangle: "))
            triangle_height = float(input("Enter the height of a triangle: "))
            print(f"The area of a triangle is: {triangleArea(triangle_base, triangle_height)}")
        case "3":
            circle_radius = float(input("Enter the radius of a circle: "))
            print(f"The area of a circle is: {circleArea(circle_radius)}")
        case "4":
            print("Exiting the program...")
        case _:
            print("Wrong input! Try again.")
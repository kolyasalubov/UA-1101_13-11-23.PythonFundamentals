from rectangle import rectangleArea
from triangle import triangleArea
from circle import circleArea

print("Use the following numbers to choose a figure and calculate its area:\n\
1. Rectangle.\n2. Triangle\n3. Circle\n\n0. Exit ")
user_input = ""
while user_input != "0":
    user_input = input("Enter you choise: ")
    match user_input:
        case "1":
            rectangle_length = float(input("Enter the length of a rectangle: "))
            rectangle_width = float(input("Enter the length of a rectangle: "))
            print(f"The area of a rectangle is: {rectangleArea(rectangle_length, rectangle_width)}\n")
        case "2":
            triangle_base = float(input("Enter the base of a triangle: "))
            triangle_height = float(input("Enter the height of a triangle: "))
            print(f"The area of a triangle is: {triangleArea(triangle_base, triangle_height)}\n")
        case "3":
            circle_radius = float(input("Enter the radius of a circle: "))
            print(f"The area of a circle is: {circleArea(circle_radius)}\n")
        case "0":
            print("Exiting the program...")
        case _:
            print("Wrong input! Try again.")
import math

def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_circle_area(radius):
    return math.pi * radius**2

user_choice = input("Enter shape (rectangle, triangle, or circle): ").lower()

if user_choice == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = calculate_rectangle_area(length, width)
elif user_choice == "triangle":
    base = float(input("Enter base length: "))
    height = float(input("Enter height: "))
    area = calculate_triangle_area(base, height)
elif user_choice == "circle":
    radius = float(input("Enter radius: "))
    area = calculate_circle_area(radius)
else:
    print("Invalid shape entered.")
    area = None

if area is not None:
    print(f"The area of the {user_choice} is: {area}")

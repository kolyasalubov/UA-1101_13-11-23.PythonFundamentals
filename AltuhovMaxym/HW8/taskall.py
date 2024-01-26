import re

def is_valid_password(password):
    
    if len(password) < 6:
        return False

    if len(password) > 16:
        return False

    if not re.search("[a-z]", password):
        return False

    if not re.search("[A-Z]", password):
        return False

    if not re.search("[0-9]", password):
        return False

    if not re.search("[$#@]", password):
        return False

    return True

user_password = input("Enter a password: ")

if is_valid_password(user_password):
    print("Password is valid.")
else:
    print("Password is invalid. Please follow the specified criteria.")
    #####next task
#     import math

# def rectangle_area(a, b):
#     return a * b

# def triangle_area(h, a):
#     return 0.5 * h * a

# def circle_area(r):
#     return math.pi * math.pow(r, 2)
# from geometry import rectangle_area, triangle_area, circle_area

# def main():
#     print("Choose a shape to calculate the area:")
#     print("1. Rectangle")
#     print("2. Triangle")
#     print("3. Circle")

#     choice = input("Enter the number of the shape (1/2/3): ")

#     if choice == "1":
#         length = float(input("Enter the length of the rectangle: "))
#         width = float(input("Enter the width of the rectangle: "))
#         area = rectangle_area(length, width)
#         print(f"The area of the rectangle is: {area}")
#     elif choice == "2":
#         base = float(input("Enter the base of the triangle: "))
#         height = float(input("Enter the height of the triangle: "))
#         area = triangle_area(height, base)
#         print(f"The area of the triangle is: {area}")
#     elif choice == "3":
#         radius = float(input("Enter the radius of the circle: "))
#         area = circle_area(radius)
#         print(f"The area of the circle is: {area}")
#     else:
#         print("Invalid choice. Please enter 1, 2, or 3.")

# if __name__ == "__main__":
#     main()
    
    
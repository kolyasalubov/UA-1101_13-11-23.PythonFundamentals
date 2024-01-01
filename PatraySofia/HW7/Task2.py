import math

def rectangle_area(length, width):
    """Calculate area of a rectangle."""
    return length * width

def triangle_area(side, length):
    """Calculate area of a triangle."""
    return 0.5 * side * length

def circle_area(pi, radius):
    """Calculate area of a circle."""
    return pi * math.pow(radius, 2)

def main():
    print("Choose a shape to calculate the area")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    user_choice = int(input("Enter the number of your choice (1, 2, or 3): "))

    if user_choice == 1:
        length = float(input("Enter the length of rectangle: "))
        width = float(input("Enter the width of rectangle: "))
        area = rectangle_area(length, width)
        print(f"The area of rectangle is: {area}")
    elif user_choice == 2:
        side = float(input("Enter the side of triangle: "))
        length = float(input("Enter the length of triangle: "))
        area = triangle_area(side, length)
        print(f"The area of triangle is: {area}")
    elif user_choice == 3:
        radius = float(input("Enter the radius of circle: "))
        area = circle_area(math.pi, radius)
        print(f"The area of circle is: {area}")
    else:
        print("Invalid choice! Enter 1, 2, or 3")

if __name__ == "__main__":
    main()

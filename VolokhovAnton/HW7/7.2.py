PI = 3.1459
def rectangle_area(length, width):
    """
    Calculates the area of a rectangle.

    Args:
    length (float): Length of the rectangle
    width (float): Width of the rectangle

    Returns:
    float: Area of the rectangle
    """
    return length * width

def triangle_area(base, height):
    """
    Calculates the area of a triangle.

    Args:
    base (float): Base of the triangle
    height (float): Height of the triangle

    Returns:
    float: Area of the triangle
    """
    return 0.5 * base * height

def circle_area(radius):
    """
    Calculates the area of a circle.

    Args:
    radius (float): Radius of the circle

    Returns:
    float: Area of the circle
    """
    return PI * radius ** 2

def main():
    print("Choose a geometrical shape to calculate its area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = rectangle_area(length, width)
        print(f"The area of the rectangle is: {area}")
    elif choice == 2:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = triangle_area(base, height)
        print(f"The area of the triangle is: {area}")
    elif choice == 3:
        radius = float(input("Enter the radius of the circle: "))
        area = circle_area(radius)
        print(f"The area of the circle is: {area}")
    else:
        print("Invalid entry. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

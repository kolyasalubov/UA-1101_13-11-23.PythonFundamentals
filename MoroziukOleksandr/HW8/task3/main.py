from geometry import rectangle_area, triangle_area, circle_area

def main():
    print("Choose the figure to calculate area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = int(input("Enter the number corresponding to the figure: "))

    if choice == 1:
        # Rectangle
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        result = rectangle_area(length, width)
        print(f"The area of the rectangle is: {result}")
    elif choice == 2:
        # Triangle
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        result = triangle_area(base, height)
        print(f"The area of the triangle is: {result}")
    elif choice == 3:
        # Circle
        radius = float(input("Enter the radius of the circle: "))
        result = circle_area(radius)
        print(f"The area of the circle is: {result}")
    else:
        print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

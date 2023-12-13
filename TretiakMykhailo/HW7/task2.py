PI = 3.14

def calculate_triangle_area(base: float, height: float) -> float:
    """Calculate the area of a triangle."""
    return 0.5 * base * height

def calculate_rectangle_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle."""
    return length * width

def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle."""
    return PI * radius**2


def main():
    
    while True:
        print("Choose a shape:")
        print("1. Triangle")
        print("2. Rectangle")
        print("3. Circle")
        print("99. Exit")
        
        choice = int(input("Enter the number of your choice: "))

        match choice:
            case 1:
                base = float(input("Enter the base of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                area = calculate_triangle_area(base, height)
                print(f"The area of the triangle is: {area}")

            case 2:
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                area = calculate_rectangle_area(length, width)
                print(f"The area of the rectangle is: {area}")

            case 3:
                radius = float(input("Enter the radius of the circle: "))
                area = calculate_circle_area(radius)
                print(f"The area of the circle is: {area}")

            case 99:
                print("Bye!")
                break
            
            case _:
                print("Invalid choice. Please enter a number between 1 and 3.")


if __name__ == "__main__":
    main()

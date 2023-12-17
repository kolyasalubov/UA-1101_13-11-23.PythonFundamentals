import geometry

def main():
    print("Select figure to calculate area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = int(input("Enter choice (1/2/3): "))

    if choice == 1:
        a = float(input("Enter length of rectangle: "))
        b = float(input("Enter width of rectangle: "))
        area = geometry.rectangle_area(a, b)
        print(f"Area of rectangle: {area}")
    elif choice == 2:
        base = float(input("Enter base of triangle: "))
        height = float(input("Enter height of triangle: "))
        area = geometry.triangle_area(base, height)
        print(f"Area of triangle: {area}")
    elif choice == 3:
        radius = float(input("Enter radius of circle: "))
        area = geometry.circle_area(radius)
        print(f"Area of circle: {area}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

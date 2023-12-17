import geometry

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    while True:
        print("Choose a figure to calculate the area:")
        print("1. Rectangle")
        print("2. Triangle")
        print("3. Circle")
        print("4. Exit")

        choice = input("Enter the number of your choice (or '4' to exit): ")

        if choice == '4':
            print("Exiting the program. Goodbye!")
            break

        if choice not in ('1', '2', '3'):
            print("Invalid choice. Please enter a number between 1 and 3.")
            continue

        if choice == '1':
            a = get_float_input("Enter the length of the rectangle: ")
            b = get_float_input("Enter the width of the rectangle: ")
            area = geometry.rectangle_area(a, b)
            print(f"The area of the rectangle is: {area}")

        elif choice == '2':
            a = get_float_input("Enter the base of the triangle: ")
            h = get_float_input("Enter the height of the triangle: ")
            area = geometry.triangle_area(a, h)
            print(f"The area of the triangle is: {area}")

        elif choice == '3':
            r = get_float_input("Enter the radius of the circle: ")
            area = geometry.circle_area(r)
            print(f"The area of the circle is: {area}")


if __name__ == "__main__":
    main()
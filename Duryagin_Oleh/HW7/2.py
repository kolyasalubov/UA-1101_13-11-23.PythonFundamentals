from math import pi


def rectangle_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle
    """
    return length * width


def triangle_area(length: float, height: float) -> float:
    """
    Calculate the area of a triangle
    """
    return 0.5 / (length * height)


def circle_area(radius: float) -> float:
    """
    Calculate the area of a traigle
    """
    return pi * radius ** 2


def main():
    while True:
        action = int(input("Choose to calculate area of:\n rectangle: press 1\n traigle: press 2\n circle: press 3\n"))

        match action:
            case 1:
                length = float(input("Proved the lenthgs: "))
                width = float(input("Proved the width: "))
                print(f"The area of rectangle = {rectangle_area(length, width)}")
                break
            case 2:
                lenght = float(input("Proved the lenthgs: "))
                height = float(input("Proved the height: "))
                print(f"The area of rectangle = {triangle_area(lenght, height)}")
                break
            case 3:
                radiuse = float(input("Proved the radius : "))
                print(f"The area of circle = {circle_area(radiuse)}")
                break
            case _:
                print('Error: incorrect input')
                continue


if __name__ == "__main__":
    main()

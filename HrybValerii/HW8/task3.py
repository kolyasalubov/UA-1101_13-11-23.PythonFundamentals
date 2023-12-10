import re


def is_convertible_float(s: str, allow_negative=False) -> bool:
    """
    The function checks whether a string literal can be converted to float.
    Returns True if the number can be converted and False if not.
    If allow_negative=False the function returns True only for positive numbers
    """
    pattern = r'^' + r'-?' * allow_negative + r'(\d+\.?\d*$|\d*\.?\d+)$'
    return bool(re.search(pattern, s))


PI = 3.14


def circle_area() -> float:
    """The function calculates the area of a circle with a given radius."""
    while True:
        radius = input("Enter the radius: ").strip()
        if is_convertible_float(radius):
            answer = PI * float(radius) ** 2
            return round(answer, 2)
        else:
            print("Radius should be a positive number")
            continue


def rectangle_area() -> float | int:
    """The function calculates the area of a rectangle with a given length and width."""
    while True:
        sides = input("Enter the length and width separated by a space: ").strip().split()
        match sides:
            case [length, width] if all([is_convertible_float(param, allow_negative=False) for param in (length, width)]):
                answer = float(length) * float(width)
                return round(answer, 2)
            case _:
                print("length and width should be two positive numbers separated by a space")
                continue


def triangle_area() -> float:
    """Function calculates area of the triangle with a known base and height"""
    while True:
        base = input(f'Enter a base of the triangle (positive number): ').strip()
        height = input(f'Enter a height of thrtriangle (positive number): ').strip()

        if is_convertible_float(base, allow_negative=False) and is_convertible_float(height, allow_negative=False):
            base, height = (float(base), float(height))
            return 0.5 * base * height
        else:
            print('''Error: values should be positive integers''')
            continue


available_shapes = {'triangle': triangle_area,
                    'rectangle': rectangle_area,
                    'circle': circle_area}


def main():
    while True:
        shape = input("Choose a shape to calculate area. Either circle, rectangle or triangle: ").strip()
        if shape in available_shapes:
            answer = available_shapes[shape]()
            print(f'The area of the {shape} is {round(answer, 2)}')
            break
        else:
            print('Error: incorrect input')
            continue


if __name__ == "__main__":
    main()

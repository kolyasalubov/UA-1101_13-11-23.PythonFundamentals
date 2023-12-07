from math import pi, sin, sqrt, radians
import re


def is_convertible_float(s: str, allow_negative=False) -> bool:
    '''
    The function checks whether a string literal can be converted to float.
    Returns True if the number can be converted and False if not
    if allow_negative=False the function returns True only for positive numbers
    '''
    pattern = r'^' + r'-?' * allow_negative + r'(\d+\.?\d*$|\d*\.?\d+)$'
    return bool(re.search(pattern, s))


def circle_area() -> float:
    '''
    The function calculates the area of a circle with a given radius.
    '''
    while True:
        radius = input("Enter the radius: ").strip()
        if is_convertible_float(radius):
            answer = pi * float(radius) ** 2
            return round(answer, 2)
        else:
            print("Radius should be a positive number")
            continue


def rectangle_area() -> float | int:
    '''
    The function calculates the area of a rectangle with a given length and width.
    '''
    while True:
        sides = input("Enter the length and width separated by a space: ").strip().split()
        match sides:
            case [length, width] if all([is_convertible_float(param, allow_negative=False) for param in (length, width)]):
                answer = float(length) * float(width)
                return round(answer, 2)
            case _:
                print("length and width should be two positive numbers separated by a space")
                continue

incorrect_input = {
    "SSS": "The input should be: SSS side1(number) side2(number) side3(number)",
    "SAS": "The input should be: SAS angle(degrees), side1(number), side2(number)",
    "HEIGHT": "The input should be: HEIGHT side base(number) height(number)",
    "ASA": "The input should be: ASA angle1 angle2 side"
}

def triangle_area() -> float:
    '''
    Function calculates area of the triangle in different ways depending on user input by usage of appropriate formulas
    It is able to calculate the area with either:
    1)three sides
    2)base and height
    3)2 sides and agle between them
    '''
    while True:
        rawinput = input(f'''Enter calculation method and parameters of the triangle, enter: 
1)SSS side1(length) side2(length) side3(length) OR
2)height base(length) height(length) OR
3)SAS angle(degrees) side1(length) side2(length)
4)ASA angle1(degrees) angle2(degrees) side(length)"
the first value is a method (SSS, SAS, HEIGHT) the rest are positive numbers separated by spaces:
''').strip().upper()
        data = rawinput.split()
        if all([is_convertible_float(num, allow_negative=False) for num in data[1:]]):
            data[1:] = [float(i) for i in data[1:]]
        else:
            print('''Error: incorrect input. 
The line should start with calculation method (SSS, SAS, height)''')
            continue

        match data:
            case ["SSS", a, b, c]:
                if sorted((a, b, c))[-1] >= sum(sorted((a, b, c))[:-1]):
                    print("Triangle with such sides does not exist")
                    continue
                p = sum((a, b, c)) / 2
                return sqrt(p * (p - a) * (p - b) * (p - c))
            case ["HEIGHT", base, height]:
                return 0.5 * base * height
            case ["SAS", angle, side1, side2]:
                return 0.5 * sin(radians(angle)) * side1 * side2
            case ["ASA", angle1, angle2, side]:
                return (side**2 * sin(radians(angle2)) * sin(radians(angle1))) / (2 * sin(radians(angle1 + angle2)))
            case [incorrect, *rest] if incorrect in incorrect_input:
                print(incorrect_input[incorrect])
                continue
            case _:
                print('Error: incorrect input')
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




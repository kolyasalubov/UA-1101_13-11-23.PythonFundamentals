import math


def rectangle_area(length, width):
    area = length*width
    return area


def triangle_area(base, height):
    area = base * height * 0.5
    return area


def circle_area(radius):
    area = math.pi * radius**2
    return area


def main(value):
    match value:
        case 1:
            length = float(input('Enter length: '))
            width = float(input('Enter width: '))
            print('Area of rectangle: ', rectangle_area(length, width))
        case 2:
            base = float(input('Enter base side: '))
            height = float(input('Enter height: '))
            print('Area of triangle: ', triangle_area(base, height))
        case 3:
            radius = float(input('Enter radius: '))
            print('Area of circle: ', circle_area(radius))
        case _:
            print('Wrong input. Try again')


print('1. Calculate rectangle area\n'
      '2. Calculate rectangle area\n'
      '3. Calculate circle area')
user_input = int(input('Choose number to perform action: '))
if __name__ == '__main__':
    main(user_input)

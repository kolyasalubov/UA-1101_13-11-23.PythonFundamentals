from math import sqrt, pi


def area_of_rectangle(length, width):
    return length * width


def area_of_triangle(side_a, side_b, side_c):
    semi_perimetr = (side_a + side_b + side_c)/2
    area = sqrt(semi_perimetr * (semi_perimetr - side_a) *
                (semi_perimetr - side_b) * (semi_perimetr - side_c))
    return round(area, 3)


def area_of_circle(radius):
    return pi * radius ** 2


def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def calculator_of_area():
    print('Choose what area you want to calculate:')
    form = int(input('1 - rectangle, 2 - triangle, 3 - circle\n'))
    if form == 1 or form == 2 or form == 3:
        match form:
            case 1:
                length = float(input('Write length: '))
                width = float(input('Write width: '))
                print('The area of rectangle with sides {} and {}: {}'
                      .format(length, width, area_of_rectangle(length=length, width=width)))
            case 2:
                side_a = float(input('Write side A: '))
                side_b = float(input('Write side B: '))
                side_c = float(input('Write side C: '))
                if is_triangle(side_a, side_b, side_c):
                    print('The area of triangle with sides {}, {} and {}:'.format(side_a, side_b, side_c),
                          round(area_of_triangle(side_a, side_b, side_c), 2))
                else:
                    print('You should write the right size of triangle. Try again')
                    calculator_of_area()
            case 3:
                radius = float(input('Write radius: '))
                print('The area of circle with radius {}:'.format(radius), round(area_of_circle(radius), 2))
    else:
        print("You don't choose any of shape. Please try again.\n")
        calculator_of_area()


# calculator_of_area()

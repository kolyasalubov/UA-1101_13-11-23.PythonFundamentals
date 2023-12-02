from math import pi, sin, sqrt
import re


def is_convertible_float(s: str, allow_negative=False)-> bool:
    '''
    The function checks whether a string literal can be converted to float.
    Returns True if the number can be converted and False if not
    if allow_negative=False the function returns True only for positive numbers
    ''' 
    pattern = r'^' + r'-?'*allow_negative + r'(\d+\.?\d*$|\d*\.?\d+)$'
    return bool(re.search(pattern, s))


def circle_area(ndigits=2) -> float:
    '''
    The function calculates the area of a circle with a given radius.
    By default, result is rounded to 2 digits, but you can specify rounding with the second argument
    '''
    while True:
        radius = input("Enter the radius: ").strip()
        if is_convertible_float(radius):
            return round(pi * float(radius)**2, ndigits)
        else:
            print("Radius should be a positive number")
            continue

        
def rectangle_area() -> float|int:
    '''
    The function calculates the area of a rectangle with a given length and width.
    '''
    while True:
        sides = input("Enter the length and width separated by a space: ").strip().split()
        match sides:
            case [length, width] if all(is_convertible_float(param, allow_negative=False) for param in (length, width)):
                return length * width
            case _:
                print("length and width should be two positive numbers separated by a space")
                continue
    

def triangle_area():
    '''
    Function calculates area of the triangle in different ways depending on user input by usage of appropriate formulas
    It is able to calculate the area with either:
    1)three sides
    2)base and height
    3)2 sides and agle between them
    '''
    while True:
        rawinput = input(f'''
Enter calculation method and parameters of the triangle: 
enter SSS side1(length) side2(length) side3(length)
or height base(length) height(length)
or SAS angle(degrees) side1(length) side2(length)
the first value is a method (SSS, SAS, height) the rest are positive numbers separated by spaces:
''').strip()
        data = rawinput.split()
        if all([is_convertible_float(num, allow_negative=False) for num in data[1:]]):
            print('''
Error: incorrect input. 
The line should start with calculation method (SSS, SAS, height)
                  ''')
            continue
        data = data[:1] + list(map(float, data[:1]))
            

        match data:
            case ["SSS", a , b, c] if all([is_convertible_float(num, allow_negative=False) for num in (a, b, c)]):
                a, b, c  = list(map(float, (a, b, c)))
                if sorted((a, b, c))[-1] >= sum(sorted((a, b, c))[:-1]): 
                    print("Triangle with such sides does not exist")
                    continue
                p = sum((a, b, c)) / 2                
                return sqrt(p * (p - a) * (p - b) * (p - c))
            case ["SSS", *rest]:
                print("The input should be: SSS side1(number) side2(number) side3(number)")
                continue
            case ["height", base, height] if base.isdigit() and height.isdigit():
                return 0.5 * base * height
            case ["height", *rest]:
                print("The input should be: sides base(number) hight(number)")
                continue
            case ["SAS", angle, side1, side2]:
                return 0.5 * sin(angle) * side1 * side2
            case ["SAS", *rest]:
                print("The input should be: angle(degrees), side1(number), side2(number)")
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
            print(available_shapes[shape]())
            break
        else:
            print('Error: incorrect input')
            continue

if __name__ == 'main':
    main()    
# print(main())       



from Module1 import *

def main():
    while True:
        action = int(input("Choose figure to calculate of:\n rectangle: press 1\n traigle: press 2\n circle: press 3\n"))

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
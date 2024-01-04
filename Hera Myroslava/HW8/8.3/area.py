import math

def area_rectangle(width, length):
    if width > 0 and length > 0:
        return length * width
    else:
        print(f"Error! Enter natural positive numbers for width and length.")
        return 0



def area_triangle (base, height):
    if base > 0 and height > 0:
        return 0.5 * base * height
    else:
        print(f"Error! Enter natural positive numbers for base and height.")
        return 0



def area_circle (radius):
    if radius > 0:
        return math.pi * math.pow(radius, 2)
    else:
        print(f"Error! Enter natural positive numbers for radius.")
        return 0
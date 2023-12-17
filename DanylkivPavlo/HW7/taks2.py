PI = 3.14

def area_of_rectangle(numr1,numr2):
    """This function determines
    the area of the rectangle"""
    sumr = numr1 * numr2
    print("The area of the rectangle is: ", sumr)
    return sumr

def area_of_triangle(height,base):
    """This function determines
    the area of the triangle"""
    sumt = 1/2 * height * base
    print("The area of the triangle is :", sumt)
    return sumt

def area_of_circle(radius):
    """This function determines
        the area of the circle"""
    sumc = PI * radius * radius
    print("The area of circle is: ", sumc)
    return sumc


user = int(input("Choose the number: \n 1. Area of rectangle \n 2. Area of triangle \n 3. Area of circle \n Enter the number: "))
if user == 1:
    numr1 = int(input("Enter the first number: "))
    numr2 = int(input("Enter the second number: "))
    area_of_rectangle(numr1, numr2)
elif user == 2:
    height = int(input("Enter the height of triangle: "))
    base = int(input("Enter the base of triangle: "))
    area_of_triangle(height, base)
else:
    radius = int(input("Enter the radius of circle: "))
    area_of_circle(radius)
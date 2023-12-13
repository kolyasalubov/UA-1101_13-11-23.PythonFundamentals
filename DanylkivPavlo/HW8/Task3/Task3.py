import functions

user = int(input("Enter number: \n 1. The area of rectangle \n 2. The area of triangle \n 3.The area of circle \n Your number is: "))

if user == 1:
    numr1 = int(input("Enter the first number: "))
    numr2 = int(input("Enter the second number: "))
    functions.area_of_rectangle(numr1, numr2)
elif user == 2:
    height = int(input("Enter the height of triangle: "))
    base = int(input("Enter the base of triangle: "))
    functions.area_of_triangle(height, base)
else:
    radius = int(input("Enter the radius of circle: "))
    functions.area_of_circle(radius)
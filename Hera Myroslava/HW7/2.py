import math
PI = math.pi

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



def area_circle (pi, radius):
    if radius > 0:
        return pi * (radius ** 2)
    else:
        print(f"Error! Enter natural positive numbers for radius.")
        return 0



def main ():
    while True:
      print("Calculate the area of the rectangle: r")
      print("Calculate the area of the triangle: t")
      print("Calculate the area of the circle: c")

      user_choice = input("Enter your choice: ")

      if user_choice == 'r':
        print(f"Enter the length and width of the rectangle:")
        length = float(input(f"Enter the length: "))
        width = float(input(f"Enter the width: "))

        area = area_rectangle(width, length)
        print(f"Area of rectangle: ", area)
        print(" ")
        break

      if user_choice == 't':
        print(f"Enter the base and height of the triangle:")
        base = float(input(f"Enter the base: "))
        height = float(input(f"Enter the height: "))

        area = area_triangle (base, height)
        print(f"Area of triangel: ", area)
        print(" ")
        break

      if user_choice == 'c':
          print(f"Enter the radius of the circle:")
          radius = float(input(f"Enter the radius: "))

          area = area_circle (PI, radius)
          print(f"Area of circle: ", area)
          print(" ")
          break

      else:
          print(f"Please, enter r, t or c")
          print(" ")

if __name__ == "__main__":
    main()
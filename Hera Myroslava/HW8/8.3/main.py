from area import area_rectangle, area_triangle, area_circle

def main ():
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

      elif user_choice == 't':
        print(f"Enter the base and height of the triangle:")
        base = float(input(f"Enter the base: "))
        height = float(input(f"Enter the height: "))

        area = area_triangle (base, height)
        print(f"Area of triangel: ", area)
        print(" ")

      elif user_choice == 'c':
          print(f"Enter the radius of the circle:")
          radius = float(input(f"Enter the radius: "))

          area = area_circle (radius)
          print(f"Area of circle: ", area)
          print(" ")

      else:
          print(f"Please, enter r, t or c")
          print(" ")

if __name__ == "__main__":
    main()
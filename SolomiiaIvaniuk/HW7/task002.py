def rectangle_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle
    """
    return length * width


def triangle_area(length: float, height: float) -> float:
    """
    Calculate the area of a triangle
    """
    return 0.5 / (length * height)


def circle_area(radius: float) -> float:
    """
    Calculate the area of a traigle
    """
    return 3.14 * radius * radius

choice = int(input("To calculate area of:\n- rectangle: put 1\n- traigle: put 2\n- circle: put 3\n"))

if choice == 1:
     length = input("Proved the lenthgs: ")
     width = input("Proved the hight: ")
     area = (float(length), float(width))
     print(f"The area of rectangle is:  {area}")
elif choice ==2:
    lenght = input("Proved the lenght: ")
    height = input ("Proved the height: ")
    area_t = (float(lenght), float(height))
    print(f"The area of traigle is:  {area_t}")
elif choice ==3:
    radius = input("Proved the radiuce: ")    
    area_c = (float(radius))
    print(f"The area of circle is:  {area_c}")
else:
      print("The incorrect choice")









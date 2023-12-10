def _rectangle(length: float, width: float) -> float:
    """
    Calculates the area of a rectangle

    :param leght: length of the rectangle
    :param width: width of the rectangle 

    :return: area of rectangle
    :type: float
    """
    return length * width

def _traigle(lenght: float, height: float) -> float:
    """
    Calculates the area of a triangle

    :param length: lenght of any side of traingle
    :param height: height of traingle

    :return: area of triangle
    :type: float
    """
    return 0.5/(lenght * height)

def _circle(radius: float) -> float:
    """
    Calculates the area of a traigle 

    :param radius: radius of circle

    :return: area of circle
    :type: float
    """
    return 3.1415 * radius * radius
  


choice = int(input("To calculate area of:\n- rectangle: put 1\n- traigle: put 2\n- circle: put 3\n"))

if choice == 1:
     length = input("Proved the lenthgs: ")
     width = input("Proved the hight: ")
     area = _rectangle(float(length), float(width))
     print(f"The area of rectangle is:  {area}")
elif choice ==2:
    lenght = input("Proved the base: ")
    height = input ("Proved the height: ")
    area_t = _traigle(float(lenght), float(height))
    print(f"The area of traigle is:  {area_t}")
elif choice ==3:
    radius = input("Proved the radiuce: ")    
    area_c = _circle(float(radius))
    print(f"The area of circle is:  {area_c}")
else:
      print("The incorrect choice")
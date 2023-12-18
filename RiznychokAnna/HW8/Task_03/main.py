import task_03_HW_08

def calculate_of_area():

    choice = int(input("""
For the calculation of areas:
- Rectangle: enter 1
- Triangle: enter 2
- Circle: enter 3
"""))


    if choice == 1:
        length = input("Enter lengths: ")
        width = input("Enter hight: ")
        area = task_03_HW_08._rectangle(float(length), float(width))
        print(f"The area of rectangle is:  {area}")
    elif choice == 2:
        lenght = input("Enter lengths: ")
        height = input("Enter height: ")
        area_t = task_03_HW_08._traigle(float(lenght), float(height))
        print(f"The area of traigle is:  {area_t}")
    elif choice == 3:
        radius = input("Enter radiuce: ")
        area_c = task_03_HW_08._circle(float(radius))
        print(f"The area of circle is:  {area_c}")
    else:
        print("The incorrect choice")

calculate_of_area()


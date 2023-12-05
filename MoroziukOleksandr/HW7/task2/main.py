# main.py

from module1 import calc_area_rectangle
from module2 import calc_area_triangle_height, calc_area_triangle_Heron, calculate_triangle_area_sas
from module3 import calc_area_triangle_circle

def main():
    
    print('This is the main program for calculating the area of geometric shapes\n')
    print('Select the area of the geometric shape you want to calculate:\n1 - Rectangle\n2 - Triangle\n3 - Circle')
    print('If you want to log out, enter - 4')

    while True:
        try:
            input_choice = int(input())
            
            if input_choice == 1: calc_area_rectangle()
                
            elif input_choice == 2:
                print('Select a method for calculating the area of a triangle:\n')
                print('1 - With height and base\n2 - With parties according to the Heron formula\n3 - By the SAS method')
                triangle_choice = int(input())
                
                if triangle_choice == 1:
                    calc_area_triangle_height()
                    
                elif triangle_choice == 2:
                    calc_area_triangle_Heron()
                    
                elif triangle_choice == 3:
                    calculate_triangle_area_sas()

                else:
                    print('Wrong choice for the triangle.')
            
            elif input_choice == 3:
                calc_area_triangle_circle()
            
            elif input_choice == 4:
                break
            
            else:
                print('Incorrect selection. Enter a number between 1 and 4.')

        except ValueError:
            print('Please enter an integer.')

if __name__ == "__main__":
    main()

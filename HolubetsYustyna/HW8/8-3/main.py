from area_calculator import rectangle_area, triangle_area, circle_area

MESSAGE_PARAM = {'r': 'Enter the height and the width (delimiter: singlespace): ',
                 't': 'Enter the baseand the height (delimiter: singlespace): ',
                 'c': 'Enter the radius: '}

while True:
    choose_figure_inp = input('Please enter the figure of your choice:\nr for rectangle\nt for triangle\nc for circle\n... ')
    if choose_figure_inp in MESSAGE_PARAM:
        break

param_inp = input(MESSAGE_PARAM[choose_figure_inp]).split()

match choose_figure_inp:
    case 'r':
        print(f'The area of your rectangle = {rectangle_area(float(param_inp[0]), float(param_inp[-1]))}')
    case 't':
        print(f'The area of your triangle = {triangle_area(float(param_inp[0]), float(param_inp[-1]))}')
    case 'c':
        print(f'The area of your circle = {circle_area(float(param_inp[0]))}')


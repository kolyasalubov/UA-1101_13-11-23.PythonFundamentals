from Calculator import area_of_rectangle, area_of_triangle, area_of_circle

def calculator_of_area():
    print('Choose what area you want to calculate:')
    form = int(input('1 - rectangle, 2 - triangle, 3 - circle\n'))
    if form == 1 or form == 2 or form == 3:
        match form:
            case 1:
                a = float(input('Write length: '))
                b = float(input('Write width: '))
                print('The area of rectangle with sides {} and {}: {}'
                      .format(a, b, area_of_rectangle(a, b)))
            case 2:
                h = float(input('Write height: '))
                a = float(input('Write base: '))
                print('The area of triangle with height {} and base {}:'.format(h, a),
                          round(area_of_triangle(h, a), 2))

            case 3:
                radius = float(input('Write radius: '))
                print('The area of circle with radius {}:'.format(radius), round(area_of_circle(radius), 2))
    else:
        print("You don't choose any of shape. Please try again.\n")
        calculator_of_area()

calculator_of_area()

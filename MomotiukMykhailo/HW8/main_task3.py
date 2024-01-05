import functions_task3

print('1. Calculate the area of a rectangle'
      '\n2. Calculate the area of a triangle'
      '\n3. Calculate the area of a circle\n')

choice = int(input('Choose the option: '))

match choice:
    case 1:
        width = int(input('Enter width: '))
        height = int(input('Enter height: '))
        print('The area of a rectangle:', functions_task3.area_rectangle(width, height))
    case 2:
        base = int(input('Enter base: '))
        height = int(input('Enter height: '))
        print('The area of a triangle:', functions_task3.area_triangle(base, height))
    case 3:
        radius = int(input('Enter radius: '))
        print('The area of a circle:', functions_task3.area_circle(radius))

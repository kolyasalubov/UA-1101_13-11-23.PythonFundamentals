class Polygon:
    """Polygon"""
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for s in range(no_of_sides)]

    def inpSides(self):
        try:
            self.sides = [float(input(f'Enter side {str(s + 1)}: ')) for s in range (self.n)]
        except:
            print('Please enter numeric values')


class Rectangle(Polygon):
    """Rectagle"""
    def __init__(self):
        super().__init__(2)

    def findArea(self):
        width, height = self.sides
        if width <= 0 or height <= 0:
            print('Please enter values > 0')
            self.inpSides()
            self.findArea()
        else:
            area = width * height
            print(f'The area of the rectangle = {area}')


rect = Rectangle()
rect.inpSides()
rect.findArea()
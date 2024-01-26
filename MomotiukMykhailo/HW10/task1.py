class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input(f'Enter side {str(i+1)}: '))
                                              for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print(f'Side {i+1} is {self.sides[i]}')


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(4)

    def findArea(self):
        a, b, c, d = self.sides
        area = a * b
        print(f'The area of a rectangle is {area}')

rect = Rectangle()
rect.inputSides()
rect.dispSides()
rect.findArea()
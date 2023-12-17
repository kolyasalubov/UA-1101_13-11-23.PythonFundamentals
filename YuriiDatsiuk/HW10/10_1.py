class Polygon():

    def __init__(self, count_sides):
        self.sides = [float(input('Enter side value ')) for x in range(count_sides)]

class Rectangle(Polygon):

    def __init__(self):
        super().__init__(2)

    def square(self):
        return self.sides[0] * self.sides[1]


rect = Rectangle()
square = rect.square()
print(f'The square of rectangle is {square}')
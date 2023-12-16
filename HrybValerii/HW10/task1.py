class Polygon:

    def __init__(self, nsides):
        self.nsides = nsides
        self.sides = [0 for _ in range(nsides)]

    def input_sides(self):
        self.sides = [int(input(f'Enter side {i}: ')) for i, _ in enumerate(self.sides, 1)]


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(4)
        self.length = self.sides[0]
        self.height = self.sides[1]

    def input_sides(self):
        self.sides = [int(input('Enter the first side(rectangle lenght): ')),
                      int(input('Enter the first side(rectangle lenght): ')), ] * 2
        self.length = self.sides[0]
        self.height = self.sides[1]

    def area(self):
        return self.length * self.height

p1 = Rectangle()
print(p1.sides)
print(p1.nsides)
p1.input_sides()
print(p1.length, p1.height)
print(f'Rectangle area is {p1.area()}')


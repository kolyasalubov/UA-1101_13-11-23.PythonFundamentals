class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def get_number_of_sides(self):
        return self.sides


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


rectangle = Rectangle(5, 8)
print(f"Number of sides: {rectangle.get_number_of_sides()}")
print(f"Area of the rectangle: {rectangle.calculate_area()}")
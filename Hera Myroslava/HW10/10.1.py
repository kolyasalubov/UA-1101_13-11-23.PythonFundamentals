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

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

rectangle = Rectangle(length, width)

print("Number of sides of the rectangle:", rectangle.get_number_of_sides())
print("Area of the rectangle:", rectangle.calculate_area())
class Polygon:
    def __init__(self, num_sides):
        self.sides = [0] * num_sides

    def input_sides(self):
        self.sides = [float(input(f"Enter the value of the side {i + 1}: ")) for i in range(len(self.sides))]

    def display_sides(self):
        for i, side in enumerate(self.sides, start=1):
            print(f"Side {i} is {side}")


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def find_area(self):
        area = self.sides[0] * self.sides[1]
        print(f'The area of the rectangle is {area:.2f}')


rectangle_instance = Rectangle()
rectangle_instance.input_sides()
rectangle_instance.display_sides()
rectangle_instance.find_area()

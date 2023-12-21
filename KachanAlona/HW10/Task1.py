class Polygon:
    def __init__(self):
        pass

class Rectangle(Polygon):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def rectangle_area(self):
        area = self.a * self.b
        print(f'The area of rectangle is {area}')


elem = Rectangle(3, 5)
elem.rectangle_area()

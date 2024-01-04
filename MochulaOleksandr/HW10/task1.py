
class Polygon():
    def __init__(self,no_of_sides):
        self.nof = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    def input_sides(self):
        self.sides = [float(input(f"Write lenth of your side{str(i+1)} ")) for i in range (self.nof)]
class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,2)
    def Rect_Area (self):
        a,b = self.sides
        area = a * b
        print(f"the area of rectangle is:{area}")


x = Rectangle()
x.input_sides()
x.Rect_Area()

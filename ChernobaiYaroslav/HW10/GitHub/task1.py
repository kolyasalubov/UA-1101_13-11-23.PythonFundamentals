class Polygon:
    
    def __init__(self, num_of_sides):
        self.sides_amount = num_of_sides
        self.sides = [0 for i in range(num_of_sides)]
    
    def addSides(self):
        self.sides = list([float(input(f"Enter side {i + 1}: ")) for i in range(self.sides_amount)])
        
    def checkSides(self):
        for i in self.sides:
            print(f"Side {self.sides.index(i) + 1}: {i}" )

class Rectangle(Polygon):
    
    def __init__(self):
        print("Enter width and height of the rectangle.")
        Polygon.__init__(self, 2)
        
    def checkSides(self):
        print(f"Width: {self.sides[0]}")
        print(f"Height: {self.sides[1]}")
        
    def calcArea(self):
        return self.sides[0] * self.sides[1]

a = Rectangle()
a.addSides()
a.checkSides()
print(f"The area of a rectangle is : {a.calcArea()}")
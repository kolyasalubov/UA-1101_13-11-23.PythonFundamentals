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
///
class Human:
    def __init__(self, name):
        self.name = name
    
    def display_welcome_message(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def species_info(cls):
        return f"You are a species of, Homosapiens."

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message."


# Example usage:
person = Human("Anton")
person.display_welcome_message()
print(Human.species_info())
print(Human.arbitrary_message())
 ///
class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def __del__(self):
        Employee.total_employees -= 1

    @classmethod
    def print_total_employees(cls):
        print(f"Total number of employees: {cls.total_employees}")

    def display_info(self):
        print(f"Employee Name: {self.name}, Salary: ${self.salary}")


employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)

Employee.print_total_employees()
employee1.display_info()
employee2.display_info()

print(f"Base classes: {Employee.__bases__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")

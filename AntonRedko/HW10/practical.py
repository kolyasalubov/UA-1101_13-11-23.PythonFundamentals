####  TASK 1 ####

class Polygon:
    def __init__(self, height, width):
        self.height = height
        self.width = width


class Rectangle(Polygon):
    def area(self):
        return self.height * self.width


# Example usage
r = Rectangle(5, 10)
print("The area of the rectangle is", r.area())


####  TASK 2  ####


class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def get_arbitrary_message():
        return "This is an arbitrary message."


# Example usage
h = Human("Alice")
h.welcome()
print(f"This person is a {h.get_species()}.")
print(Human.get_arbitrary_message())

####  TASK 3 ####


class Employee:
    num_of_emps = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num_of_emps += 1

    def display_employee(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def display_total_employees(cls):
        print(f"Total employees: {cls.num_of_emps}")


# Example usage
e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)
e3 = Employee("Charlie", 70000)

e1.display_employee()
e2.display_employee()
e3.display_employee()

Employee.display_total_employees()

# Displaying information about the class
print(f"Base classes: {Employee.__base__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")

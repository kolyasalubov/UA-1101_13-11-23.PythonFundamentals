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

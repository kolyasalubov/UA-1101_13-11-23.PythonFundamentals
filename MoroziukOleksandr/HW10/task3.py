class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        # Increment total employees on object creation
        Employee.total_employees += 1

    def __str__(self):
        return f"Employee: {self.name}, Salary: ${self.salary:.2f}"

    @classmethod
    def print_total_employees(cls):
        print(f"Total Employees: {cls.total_employees}")

    @staticmethod
    def class_info():
        print(f"Base classes: {Employee.__bases__}")
        print(f"Class namespace: {Employee.__dict__}")
        print(f"Class name: {Employee.__name__}")
        print(f"Module name: {Employee.__module__}")
        print(f"Class documentation: {Employee.__doc__}")

emp1 = Employee("John Doe", 50000)
emp2 = Employee("Jane Smith", 45000)

print(emp1)
print(emp2)

Employee.print_total_employees()
Employee.class_info()

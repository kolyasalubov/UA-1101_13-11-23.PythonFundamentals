class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
        Employee.total_employees += 1

    def display_employee_info(self):
        print(f"Employee Name: {self.name}, Salary: ${self.salary}")

    @classmethod
    def display_total_employees(cls):
        print(f"Total Employees: {cls.total_employees}")

print("Class Inheritance:", Employee.__base__)
print("Class Namespace:", Employee.__dict__)
print("Class Name:", Employee.__name__)
print("Module Name:", Employee.__module__)
print("Documentation:", Employee.__doc__)

employee1 = Employee("John Doe", 50000)
employee2 = Employee("Jane Smith", 60000)
employee3 = Employee("Adam Felton", 5500)

employee1.display_employee_info()
employee2.display_employee_info()
employee3.display_employee_info()

Employee.display_total_employees()
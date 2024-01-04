class Employee:
    """

Employee class with counter of the created objects.
Every object has name and salary.

    """
    _counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee._counter += 1

    def showEmployeeInfo(self):
        print(f"{self.name}'s salary is {self.salary}")

    @classmethod
    def __del__(cls):
        Employee._counter -= 1

    @classmethod
    def showEmployeesCount(cls):
        print(f"The number of employees: {Employee._counter}")


a = Employee("Carry", 600)
b = Employee("Bob", 2000)
a.showEmployeesCount()
del b
a.showEmployeesCount()
a.showEmployeeInfo()

print(f"\n{Employee.__name__} is inhereted from the {Employee.__base__}, \
called in {Employee.__module__} module and has \
namespace: {Employee.__dict__}\n")
print(f"The documenntation of the\
{Employee.__name__} class: {Employee.__doc__}")
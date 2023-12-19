class Employee():
    """Create employee"""

    counter_employee = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter_employee += 1

    @classmethod
    def count_employee(cls):
        print(f'count of employees - {cls.counter_employee}')

    @classmethod
    def infoCLS(cls, instance):
        print(f'name = {instance.name} salary = {instance.salary}')

    def infoINS(self):
        print(f'name = {self.name} salary = {self.salary}')


e1 = Employee('First', 10000)
e2 = Employee('Second', 5000)
e1.infoINS()
e2.infoINS()

Employee.count_employee()
Employee.infoCLS(e1)
Employee.infoCLS(e2)

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
class Employee:
    counter = 0
    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary

    def __del__(self):
        Employee.counter -= 1

    def count_employees(self):
        print(f'Quantity of employees at the moment: {self.counter}')

    def info_employee(self):
        print(f'Name: {self.name}, salary: {self.salary}')

    def info_classes(self):
        print(f'Other clases: '
              f'\nbase: {Employee.__base__}'
              f'\nclass namespace: {Employee.__dict__}'
              f'\nclass name: {Employee.__name__}'
              f'\nmodule name in which class defined: {Employee.__module__}'
              f'\ndocumentation bar: {Employee.__doc__}')


employee_1 = Employee('Michael', '3000')
employee_2 = Employee('Sally', '1500')
employee_3 = Employee('Jack', '2000')

employee_1.count_employees()
employee_1.info_employee()
employee_2.info_employee()
employee_1.info_classes()
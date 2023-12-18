class Employee:
    """A class representing an employee.

    Attributes:
        counter (int): A class variable to keep track of the total number of employees.

    Methods:
        number_of_employees(): A class method that returns the total number of employees.
        __init__(name, salary): Initializes an employee with a name and salary.
        info(): Returns information about the employee.
    """
    counter = 0

    @classmethod
    def number_of_employees(cls):
        return f'There are/is {cls.counter} employee(s) hired.'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1
        print(f'{self.name} was hired.')

    def __del__(self):
        print(f'{self.name} was fired(.')
        Employee.counter -= 1

    def info(self):
        return f'''This employee`s name is {self.name}
his salary is {self.salary} $ per month.'''


John = Employee('John', 1000)
print(John.info())
print(Employee.number_of_employees())
del John
print(Employee.number_of_employees())

print(f'\nBase classes from which the Employee class is inherited is {Employee.__base__}')
print(f'Employee class namespace: {Employee.__dict__}.')
print(f'Employee class is defined inside {Employee.__module__} module.')
print(f'Documentation on Emloyee class: \n{Employee.__doc__}')


class Employee:
    """Class for initialisation Employee"""
    counter = 0

    def __init__(self, name, surname, salary):
        Employee.counter += 1
        self.name = name
        self.surname = surname
        self.salary = salary

    def __del__(self):
        Employee.counter -= 1

    @staticmethod
    def emploees_amount():
        print(f'The total amount of emploees are {Employee.counter}.')

    def get_info(self):
        print(f'Emploee {self.name} {self.surname} has salary {self.salary}.')

    def __str__(self):
        return f'Emploee {self.name} {self.surname}.'

    @classmethod
    def inner_info(cls):
        print(f'Class "{cls.__name__}" inherits class "{cls.__base__.__name__}".')
        print('Class namespaces:')
        for key in cls.__dict__:
            print(key)
        print(f'Module name in which the class is defined: {cls.__module__}')
        print(f'Documentation bar: {cls.__doc__}')



# em1 = Employee('Anna', 'Bo', 5000)
# em2 = Employee('Bob', 'Ru', 3000)
# em3 = Employee('Catty', 'Dou', 8000)
#
# print(em1.name, em1.surname, em1.salary, em1.counter)
# print(em2.name, em2.counter)
# Employee.emploees_amount()
# em1.get_info()
# print(em2)
# Employee.inner_info()

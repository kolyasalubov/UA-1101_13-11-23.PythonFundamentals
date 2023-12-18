class Employee:
    """
    Employee's info: name and salary
    """
    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    def __del__(self):
        Employee.counter -= 1

    @classmethod
    def EmployeesTotal(cls):
        print(f'The total number of employees: {cls.counter}')

    def _get_EmployeeInfo(self):
        print(f'Name: {self._name}. Salary: {self._salary}')

    def _get_name(self):
        return self._name
    
    def _get_salary(self):
        return self._salary

    def _set_name(self, newname):
        self._name = newname
    
    def _set_salary(self, newsalary):
        self._salary = newsalary
    
    def del_name(self):
        del(self._name)
    
    def del_salary(self):
        del(self._salary)

    name = property(_get_name, _set_name, del_name)
    salary = property(_get_salary, _set_salary, del_salary)


print(Employee.__base__)
print(Employee.__dict__)
print(Employee.name)
print(Employee.__module__)
print(Employee.__doc__)

empl_1 = Employee('Tom', 1000)
Employee.EmployeesTotal()
empl_1._get_EmployeeInfo()
empl_1.salary = 2000
print(empl_1._get_salary())


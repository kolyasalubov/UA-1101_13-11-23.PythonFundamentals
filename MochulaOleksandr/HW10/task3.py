class Employee():

    total_employee = 0
    all_employee_dict = {}

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.total_employee +=1

    def print_totoal_employee(self):
        print(f"Total number of employee: {Employee.total_employee}")
    
    def print_employee_info(self):
        print("Name:",self.name)
        print("Salary:",self.salary)

    def print_dict(self):
            Employee.all_employee_dict [self.name] = self.salary
            print(Employee.all_employee_dict)

employee_1 = Employee("Richard",40000)
employee_2 = Employee("John:",50000)
employee_3 = Employee("Lily",10000)

employee_1.print_totoal_employee()

employee_3.print_dict()

employee_1.print_employee_info() 
employee_2.print_employee_info()
employee_3.print_employee_info()

print("Base classes:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)

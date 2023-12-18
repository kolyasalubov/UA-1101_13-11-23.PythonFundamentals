class Employee:
    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    @staticmethod
    def total_number_of_employee():
        print(f"\nThe total numbers of employee are: {Employee.counter}")

    def information_about_each_employee(self):
        print(self.name, self.salary)


employee_1 = Employee("Margo", 575)
employee_1.information_about_each_employee()
employee_2 = Employee("Valentyna", 233)
employee_2.information_about_each_employee()
employee_3 = Employee("Ivan", 3455)
employee_3.information_about_each_employee()
employee_4 = Employee("Marko", 575)
employee_4.information_about_each_employee()
Employee.total_number_of_employee()

employee_class_info = {
    "__base__": Employee.__base__,
    "__dict__": Employee.__dict__,
    "__name__": Employee.__name__,
    "__module__": Employee.__module__,
    "__doc__": Employee.__doc__,
}
print(employee_class_info)
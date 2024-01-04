class Employee:
    total_employees = 0
    employee_list = []

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1
        Employee.employee_list.append({"name": self.name, "salary": self.salary})

    @classmethod
    def total_number_of_employees(cls):
        print(f"\nThe total number of employees is: {cls.total_employees}")

    @staticmethod
    def employee_information():
        for emp in Employee.employee_list:
            print(f"Name: {emp['name']}, Salary: {emp['salary']}")

    @classmethod
    def class_info(cls):
        return {
            "__base__": cls.__base__,
            "__dict__": cls.__dict__,
            "__name__": cls.__name__,
            "__module__": cls.__module__,
            "__doc__": cls.__doc__,
        }


# Example usage:
employee_1 = Employee("Anton", 50000)
employee_2 = Employee("Igor", 35000)
employee_3 = Employee("Gundeep", 15000)
employee_4 = Employee("Gurpreet", 575)

Employee.employee_information()
Employee.total_number_of_employees()

print(Employee.class_info())

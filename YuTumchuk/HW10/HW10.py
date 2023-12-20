############### Task1 ####################
# class Polygon:
#     def __init__(self, number_of_measurements, name):
#         self.measurement=number_of_measurements
#         self.shapename=name
#         print(f"Let make some calculations with your {self.shapename}.")
#         self.sides=[input("Enter sidelength:") for x in range(self.measurement)]
#
# class Rectangle(Polygon):
#     def __init__(self,  number_of_measurements=2, name="Rectangle"):
#         super().__init__(number_of_measurements,name)
#         self.square = int(self.sides[0])*int(self.sides[1])
#         print(f"The square is {self.square}.")
#
# n=Rectangle()
# z=Polygon(5,"Pentagon")

############### Task2 ####################
# class Human:
#     males = 0
#     females = 0
#
#     def __init__(self, name, sex):
#         self.name = name
#         self.sex = sex
#         Human.males += 1 if self.sex == "Male" else 0
#         Human.females += 1 if self.sex == "Female" else 0
#
#     def welcome_msg(self):
#         if self.sex == "Male":
#             print(f"Welcome, dear Sir {self.name}!")
#         else:
#             print(f"Welcome dear Madam {self.name}!")
#
#     @classmethod
#     def species(cls):
#         print(f"All of the invided are Homosapiens and totally {cls.males} males and {cls.females} females by sex.")
#
#     def msg(self):
#         print("We are glad to have you here at our event!")
#
#
# guest1 = Human("Joe", "Male")
# guest2 = Human("Paul", "Male")
# guest3 = Human("Maria", "Female")
# guest1.welcome_msg()
# guest1.msg()
# guest2.welcome_msg()
# guest1.msg()
# guest3.welcome_msg()
# guest1.msg()
# Human.species()

############### Task3 ####################

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class MyOrganization:
    """Allow to maintain the database of employees"""

    def __init__(self, company_name):
        self.company_name = company_name
        self.people = []
        self.totally_people = 0

    def hire_someone(self, name, salary):
        newcomer = Employee(name, salary)
        self.people.append(newcomer)
        self.totally_people += 1

    def show_all(self):
        for item in self.people:
            print(f"{item.name} with salary {item.salary}$")

    def show_employee(self, name):
        for item in self.people:
            if item.name == name:
                print(f"Hi, {item.name}, you are paid {item.salary} monthly!")

ms = MyOrganization("Microsoft")
ms.hire_someone("Jack", 1000)
ms.hire_someone("Ronnie", 1500)
ms.hire_someone("Amanda", 2000)
print(f"We hired {ms.totally_people} people in staff.")
ms.show_all()
ms.show_employee("Amanda")
print(MyOrganization.__base__)
print(MyOrganization.__dict__)
print(MyOrganization.__name__)
print(MyOrganization.__module__)
print(MyOrganization.__doc__)

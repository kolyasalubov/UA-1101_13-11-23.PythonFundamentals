class AgeChecker:
    def __init__(self):
        self.age = 0

    def get_age(self):
        self.age = int(input("Enter your age: "))
        if self.age < 0:
            raise ValueError("Age cannot be negative")

    def check_age(self):
        if self.age % 2 == 0:
            print(f"{self.age} is even")
        else:
            print(f"{self.age} is odd")


age_checker = AgeChecker()
try:
    age_checker.get_age()
    age_checker.check_age()
except ValueError as e:
    print(e)

class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        print(f"Welcome, {self.name}")

    def information(self):
        return f"{self.name}, you are Homosapiens"

    @staticmethod
    def message():
        return "We are all Homosapiens"


Vasia = Human("Vasia")
Vasia.welcome_message()
print(Vasia.information())
Oleh = Human("Oleh")
Oleh.welcome_message()
print(Oleh.information())
print(Human.message())

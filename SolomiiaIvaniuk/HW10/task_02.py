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


Misha = Human("Misha")
Misha.welcome_message()
print(Misha.information())
Solomiia = Human("Solomiia")
Solomiia.welcome_message()
print(Solomiia.information())
print(Human.message())

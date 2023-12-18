class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        print(f"Welcome, {self.name}")

    def inform(self):
        return f"{self.name}, you are Homosapiens"

    @staticmethod
    def message():
        return "We are all Homosapiens"      
#####arbitrary message#####

ivan = Human("Ivan")
ivan.welcome_message()
print(ivan.inform())
anna = Human("Anna")
anna.welcome_message()
print(anna.inform())
print(Human.message())

class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Hello, {self.name}! Welcome!"

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def arbitrary_message():
        return "This is a static method with an arbitrary message."


person = Human("John")
print(person.say_hello())
print(f"Species: {Human.get_species()}")
print(Human.arbitrary_message())

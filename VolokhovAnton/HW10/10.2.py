class Human:
    def __init__(self, name):
        self.name = name
    
    def display_welcome_message(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def species_info(cls):
        return f"You are a species of, Homosapiens."

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message."


# Example usage:
person = Human("Anton")
person.display_welcome_message()
print(Human.species_info())
print(Human.arbitrary_message())
 
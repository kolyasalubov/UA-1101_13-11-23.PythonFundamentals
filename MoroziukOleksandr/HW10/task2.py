class Human:
  def __init__(self, name):
    self.name = name

  def welcome_message(self):
    print(f"Welcome, {self.name}!")

  @classmethod
  def species(cls):
    return "Homosapiens"

  @staticmethod
  def random_message():
    return "This is a random message from the Human class."

person1 = Human("Oleg")
person1.welcome_message()

print(Human.species())
print(Human.random_message())

class Human:
   def __init__(self, name):
     self.name = name
    
   def message(self):
     print(f"Hello, {self.name}!")

   def info(self):
     return f"{self.name} a species of - Homosapiens."

   @staticmethod
   def message_for_user():
     return "Welcome!"

person1 = Human("Robert")
person1.message()
print(Human.message_for_user())
print(person1.info())  # Note the change here, use person1 instead of Human

person2 = Human("Johnny")
person2.message()
print(person2.info())  # Note the change here, use person2 instead of Human
print(Human.message_for_user())

person3 = Human("Sophie")
person3.message()
print(person3.info())  # Note the change here, use person3 instead of Human
print(Human.message_for_user())
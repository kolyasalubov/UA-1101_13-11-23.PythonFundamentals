class Human():
    
    def __init__(self, name):
        self.name = name
    
    def sayHello(self):
        print(f"Hello, {self.name}.")
    
    @classmethod
    def species(cls):
        return(f"The {cls.__name__} is a species of Homosapiens.")
        
    @staticmethod
    def stMethod():
        print("This is a static method.")
        
human1 = Human("Denny")
human1.sayHello()
print(human1.species())
human1.stMethod()

print("\n", end="")

human2 = Human(input("Enter a name: "))
human2.sayHello()
print(human2.species())
human1.stMethod()

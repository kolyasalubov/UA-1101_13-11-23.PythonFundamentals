class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name):
        super().__init__(name)

class Woman(Human):
    def __init__(self, name):
        super().__init__(name)

def create_god():
    adam = Man("Adam")
    eve = Woman("Eve")
    return [adam, eve]

# Example usage
adam, eve = create_god()
print(f"{adam.name} is a {type(adam).__name__}")
print(f"{eve.name} is a {type(eve).__name__}")

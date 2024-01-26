class Human:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hello {self.name}!')

    def species(self):
        print('Every human belongs to Homosapiens species')

    @staticmethod
    def static_hello():
        print('Hello, I\'m static method!')
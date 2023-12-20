class Human:
    def __init__(self, name):
        self.name = name

    def greating(self):
        print(f'Hello, {self.name}!')

    @classmethod
    def species(cls):
        print('This is a species of "Homosapiens".')

    @staticmethod
    def just_info():
        print('World Population Clock: 8.1 Billion People')


# human1 = Human('Anna')
# human1.greating()
# Human.species()
# human1.species()
# human1.just_info()
# Human.just_info()

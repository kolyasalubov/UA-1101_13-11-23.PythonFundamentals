class Human():

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f'welcome {self.name}')

    @classmethod
    def species(cls):
        print('Its homosapiens')
        
    @staticmethod
    def the_best_of():
        print('There are alot of Human, but you are the best')

human = Human('Valera')
human.welcome()
human.species()
human.the_best_of()
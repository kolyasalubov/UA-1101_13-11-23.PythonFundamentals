class Human:
    """Human: name, species"""
    def __init__(self, name):
        self.name = name
    
    def welcomeMsg(self):
        print(f'Greetings, {self.name}!')

    @classmethod
    def Species(cls):
        return 'Homo sapiens'
    
    @staticmethod
    def Msg():
        print('You are one of the 8.1 billion of your species.')


hum_1 = Human(input('What is your name? '))
hum_1.welcomeMsg()
print(f'{Human.Species()} have been inhabiting the Earth for the past 200 000 years.')
hum_1.Msg()
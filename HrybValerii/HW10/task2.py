class Human:
    @classmethod
    def species(cls):
        return 'This is the species of Homosapiens'

    @staticmethod
    def show_message():
        return 'I am a human)'

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"Welcome, {self.name}")

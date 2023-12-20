class Human():
    def __init__(self,name):
        self.num_names = name
        self.names = [0 for i in range(name)]
    def input_name(self):
        self.names = [(input(f"What is your name dude{ str(i+1)}?: ")) for i in range (self.num_names)]
    def welcome(self):
        for i in range(self.num_names):
            print(f"Hello my dear {self.names[i]}")
class Homosapiens(Human):
    def __init__(self):
        Human.__init__(self,int(input("How many peoples are there?")))
    def you_homo(self):
        for i in range(self.num_names):
            self.homo = {self.names[i] : "Homosapiens"}
            print(self.homo)
    def static():
        return print("We all are Humans")

x = Homosapiens()
x.input_name()
x.welcome()
x.you_homo()
Homosapiens.static()
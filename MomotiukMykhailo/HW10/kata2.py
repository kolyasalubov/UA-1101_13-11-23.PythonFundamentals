import random
class Ghost(object):
    def __init__(self, color = None):
        value = random.randint(1, 4)
        match value:
            case 1:
                self.color = 'white'
            case 2:
                self.color = 'yellow'
            case 3:
                self.color = 'purple'
            case 4:
                self.color = 'red'
# I have seen the best solution on codewars with random.choice but I'd like to leave my first thought
# class Ghost(object):
#   def __init__(self):
#     self.color = random.choice(["white", "yellow", "purple", "red"])
"""
https://www.codewars.com/kata/basic-subclasses-adam-and-eve

Description:
According to the creation myths of the Abrahamic religions,
Adam and Eve were the first Humans to wander the Earth.

You have to do God's job. The creation method must return an array 
of length 2 containing objects (representing Adam and Eve).
The first object in the array should be an instance of the class Man.
The second should be an instance of the class Woman.
Both objects have to be subclasses of Human.
Your job is to implement the Human, Man and Woman classes.
"""

class Human:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")


class Man(Human):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} says: Hello, I am a man."


class Woman(Human):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} says: Hello, I am a woman."


def God():
    adam = Man("Adam")
    eve = Woman("Eve")

    return [adam, eve]


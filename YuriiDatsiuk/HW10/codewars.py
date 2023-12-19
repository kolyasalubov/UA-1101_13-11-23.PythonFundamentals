# I. Ball-super-ball
#Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
class Ball(object):
    def __init__(self, type='regular'):
        self.ball_type = type
# II. Color-ghost
#Create a class Ghost
# Ghost objects are instantiated without any arguments.
# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
import random
class Ghost(object):
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        rnd = random.randint(1,len(colors))
        self.color = colors[rnd-1]

# III. Basic-subclasses-Adam-and-Eve
#According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.
# You have to do God's job. The creation method must return an array of length 2 containing objects (representing Adam and Eve).
# The first object in the array should be an instance of the class Man. The second should be an instance of the class Woman.
# Both objects have to be subclasses of Human. Your job is to implement the Human, Man and Woman classes.
import numpy

class Human():
    pass
class Man(Human):
    pass
class Woman(Human):
    pass
def God():
    return numpy.array([Man(), Woman()])

# IV. Classy-classes
# Your task is to complete this Class, the Person class has been created.
# You must fill in the Constructor method to accept a name as string and an age as number,
# complete the get Info property and getInfo method/Info getter which should return johns age is 34
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name}s age is {self.age}"

    info = property(get_info)

# V. Building Spheres
#Now that we have a Block let's move on to something slightly more complex: a Sphere.
from math import pi
class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_volume(self):
        return round((4 / 3) * pi * self.radius ** 3, 5)
    def get_surface_area(self):
        return round(4 * pi * self.radius ** 2, 5)
    def get_density(self):
        return round(self.mass / self.get_volume(), 5)

# VI. Dynamic Classes
import re
def class_name_changer(cls, new_name):
    if re.match(r'^[A-Z][a-zA-Z0-9]*$', new_name):
        cls.__name__ = new_name
    else:
        raise Exception


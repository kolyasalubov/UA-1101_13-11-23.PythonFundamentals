# Regular Ball Super Ball
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

# Color Ghost
from random import choice


class Ghost(object):
    def __init__(self):
        self.color = choice(("white", "yellow", "purple", "red"))


# Basic subclasses - Adam and Eve
def God():
    Adam = Man('Adam')
    Eve = Woman('Eve')
    return (Adam, Eve)


class Human:
    def __init__(self, name):
        self.name = name


class Man(Human):
    def __init__(self, name):
        super().__init__(name)


class Woman(Human):
    def __init__(self, name):
        super().__init__(name)

# Classy Classes
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"

    def get_info(self):
        return self.info


# Building Spheres
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
        return round(4 * pi * self.radius ** 3 / 3, 5)

    def get_surface_area(self):
        return round(4 * pi * self.radius ** 2, 5)

    def get_density(self):
        return round(self.get_mass() / self.get_volume(), 5)


# Python's Dynamic Classes #1
from string import ascii_uppercase


def class_name_changer(cls, new_name):
    if new_name[0] in ascii_uppercase and new_name.isalnum():
        cls.__name__ = new_name
    else:
        raise Exception

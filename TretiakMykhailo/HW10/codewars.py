class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

#----------------------------------------------------------

import random
class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "red", "yellow", "purple"])


#----------------------------------------------------------

class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name):
        super().__init__(name)

class Woman(Human):
    def __init__(self, name):
        super().__init__(name)

def God():
    adam = Man("Adam")
    eve = Woman("Eve")
    return [adam, eve]


#----------------------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f'{name}s age is {age}'


#----------------------------------------------------------

import math
class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4 / 3) * math.pi * (self.radius ** 3)
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * math.pi * (self.radius ** 2)
        return round(surface_area, 5)

    def get_density(self):
        density = self.mass / self.get_volume()
        return density

#----------------------------------------------------------

def class_name_changer(cls, new_name):
    exec(f"class {new_name}({cls.__name__}): pass")


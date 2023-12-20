# Task 1 Regular Ball Super Ball
import re
import math
import random


class Ball:
    def __init__(self, ball_type="Regular"):
        self.ball_type = ball_type


# Example usage
b1 = Ball()
b2 = Ball("Super")

print(f"Ball 1 type: {b1.ball_type}")
print(f"Ball 2 type: {b2.ball_type}")

# Task 2 Ghost Class

class Ghost:
    def __init__(self):
        self.color = random.choice(["White", "Yellow", "Purple", "Red"])


# Example usage
g1 = Ghost()
g2 = Ghost()

print(f"Ghost 1 color: {g1.color}")
print(f"Ghost 2 color: {g2.color}")

# Task 3 Adam and Eve


class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


def God():
    return [Man(), Woman()]


# Example usage
people = God()
print(type(people[0]))  # <class '__main__.Man'>
print(type(people[1]))  # <class '__main__.Woman'>

#Task 4 Person Class

class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age
        self.info = "{0.name}s age is {0.age}".format(self)

#Task 5 Sphere Class 


class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4/3) * math.pi * (self.radius ** 3)
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * math.pi * (self.radius ** 2)
        return round(surface_area, 5)

    def get_density(self):
        density = self.mass / self.get_volume()
        return round(density, 5)

#Task6 Dynamic Class Creation

def class_name_changer(cls, new_name):
    if re.match(r'^[A-Z][a-zA-Z0-9-_]*$', new_name):
        cls.__name__ = new_name
    else:
        raise Exception('Invalid Class Name')

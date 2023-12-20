#### TASK 1 ####
# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
import re
import math
import random


class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


# Example usage
b1 = Ball()
b2 = Ball("super")

print(f"Ball 1 type: {b1.ball_type}")
print(f"Ball 2 type: {b2.ball_type}")

#### TASK 2 ####

# Create a class Ghost
# Ghost objects are instantiated without any arguments.
# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated


class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


# Example usage
g1 = Ghost()
g2 = Ghost()

print(f"Ghost 1 color: {g1.color}")
print(f"Ghost 2 color: {g2.color}")

#### TASK 3 ####
# According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.
# You have to do God's job. The creation method must return an array of length 2 containing objects (representing Adam and Eve).
# The first object in the array should be an instance of the class Man.
# The second should be an instance of the class Woman.
# Both objects have to be subclasses of Human. Your job is to implement the Human, Man and Woman classes.


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

#### TASK 4 ####
# Your task is to complete this Class, the Person class has been created.
# You must fill in the Constructor method to accept a name as string and an age as number, complete the get Info property and getInfo method/Info getter which should return johns age is 34


class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age
        self.info = "{0.name}s age is {0.age}".format(self)

#### TASK 5 ####
# Now that we have a Block let's move on to something slightly more complex: a Sphere.


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

#### TASK 6 ####

# Dynamic Classes


def class_name_changer(cls, new_name):
    if re.match(r'^[A-Z][a-zA-Z0-9-_]*$', new_name):
        cls.__name__ = new_name
    else:
        raise Exception('Invalid Class Name')

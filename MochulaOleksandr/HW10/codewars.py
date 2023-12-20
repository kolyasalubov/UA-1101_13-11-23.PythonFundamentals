class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type
#1 kata

import random

class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])
#2 kata
        
#3 kata unfortunatelly I have no idea
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"
#4 kata
class Sphere(object):
    def __init__(self,radius,mass):
        self.radius = radius
        self.mass = mass
    def get_radius(self):
        print(self.radius)
    def get_mass(self): 
        print(self.mass)
    def get_volume(self):
        self.volume = 4/3* 3.14159* (self.radius **3)
        self.volume = round(self.volume,5)
        print(self.volume)
    def get_surface_area(self):
        print(4*3.14159*(self.radius**2))
    def get_density(self):
        self.dentisy = self.mass / self.volume
        self.dentisy = round(self.dentisy,5)
        print(self.dentisy)
#5 kata
def class_name_changer(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
        raise ValueError("Invalid class name.")
    cls.__name__ = new_name
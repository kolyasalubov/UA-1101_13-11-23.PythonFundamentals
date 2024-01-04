############# Task 1 ##################
"""Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
If no arguments are given, ball objects should instantiate with a "ball type" of "regular.""""
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type=ball_type
############# Task 2 ##################
"""Create a class Ghost
Ghost objects are instantiated without any arguments.
Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
ghost = Ghost()"""
from random import randint
class Ghost(object):
    col_options=["white","yellow","purple","red"]
    def __init__(self):
        self.color=Ghost.col_options[randint(0,3)]
############# Task 3 ##################
"""According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.
You have to do God's job. The creation method must return an array of length 2 containing objects 
(representing Adam and Eve). The first object in the array should be an instance of the class Man. 
The second should be an instance of the class Woman. Both objects have to be subclasses of Human. 
Your job is to implement the Human, Man and Woman classes."""


def God():
    man = Man()
    woman = Woman()
    return [man, woman]


class Human:
    def __init__(self):
        self.creature = "human"


class Man(Human):
    def __init__(self):
        super().__init__()
        self.sex = "Man"


class Woman(Human):
    def __init__(self):
        super().__init__()
        self.sex = "Woman"

############# Task 4 ##################

"""Your task is to complete this Class, the Person class has been created. 
You must fill in the Constructor method to accept a name as string and an age as number, 
complete the get Info property and getInfo method/Info getter which should return johns age is 34"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"

############# Task 5 ##################
"""Building Spheres
Arguments for the constructor
radius -> integer or float (do not round it)
mass -> integer or float (do not round it)
Methods to be defined
get_radius()       =>  radius of the Sphere (do not round it)
get_mass()         =>  mass of the Sphere (do not round it)
get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
get_density()      =>  density of the Sphere (rounded to 5 place after the"""
from math import pi,pow
class Sphere(object):
  def __init__(self,radius,mass):
    self.radius = radius
    self.mass = mass
  def get_radius(self):
    return self.radius
  def get_mass(self):
    return self.mass
  def get_volume(self):
    return round(4/3*pi*pow(self.radius,3),5)
  def get_surface_area(self):
    return round(4*pi*pow(self.radius,2),5)
  def get_density(self):
    return round(self.mass/(4/3*pi*pow(self.radius,3)),5)
############# Task 6 ##################
"""Timmy's quiet and calm work has been suddenly stopped by his project manager (let's call him boss) yelling:

- Who named these classes?! Class MyClass? It's ridiculous! I want you to change it to UsefulClass!

Tim sighed, he already knew it's gonna be a long day.
Few hours later, boss came again:
Much better - he said - but now I want to change that class name to SecondUsefulClass,

and went off. Although Timmy had no idea why changing name is so important for his boss, he realized, that it's 
not the end, so he turned to you, his guru, to help him and asked you to prepare some function, which could change 
name of given class.
Note: Proposed function should allow only names with alphanumeric chars (upper & lower letters plus ciphers), 
but starting only with upper case letter. In other case it should raise an exception.
Disclaimer: there are obviously betters way to check class name than in example cases, but let's stick with that, 
that Timmy yet has to learn them."""

def class_name_changer(cls, new_name):
    if new_name[0].isupper() and new_name.isalnum() and not new_name and not new_name[0].isdigit() and not \
            new_name.isidentifier():
        cls.__name__=new_name
    else:
        raise Exception ("bad name")
"""
https://www.codewars.com/kata/color-ghost
Description:
Create a class Ghost
Ghost objects are instantiated without any arguments. Ghost objects are 
given a random color attribute of "white" or "yellow" or "purple" 
or "red" when instantiated.
"""
import random

class Ghost(object):
   def __init__(self):
       colors = ["white", "yellow", "purple", "red"]
       self.color = random.choice(colors)
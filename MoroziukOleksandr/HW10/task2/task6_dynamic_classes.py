"""
https://www.codewars.com/kata/55ddb0ea5a133623b6000043
Description:
Timmy's quiet and calm work has been suddenly stopped by his project 
manager (let's call him boss) yelling:

- Who named these classes?! Class MyClass? It's ridiculous!
I want you to change it to UsefulClass!

Tim sighed, he already knew it's gonna be a long day.
Few hours later, boss came again:
Much better - he said - but now I want to change that class name to 
SecondUsefulClass, and went off. Although Timmy had no idea why changing
name is so important for his boss, he realized, that it's not the end,
so he turned to you, his guru, to help him and asked you to prepare some
function, which could change name of given class.
Note: Proposed function should allow only names with alphanumeric chars
(upper & lower letters plus ciphers), but starting only with upper case
letter. In other case it should raise an exception.
Disclaimer: there are obviously betters way to check class name than in
example cases, but let's stick with that,
that Timmy yet has to learn them.
"""
def class_name_changer(cls, new_name):
  # Validate new name format
  if not new_name[0].isupper():
    raise ValueError("Class name must start with an uppercase letter.")

  if not all(char.isalnum() for char in new_name):
    raise ValueError("Class name can only contain alphanumeric characters.")

  # Update class name
  cls.__name__ = new_name

  # Inform user of successful change
  print(f"Class renamed from '{cls.__name__}' to '{new_name}'.")
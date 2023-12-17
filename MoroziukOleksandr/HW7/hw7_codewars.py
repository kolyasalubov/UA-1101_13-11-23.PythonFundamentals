# I. Jenny's secret message.
"""
DESCRIPTION:
Task - Jenny has written a function that returns a greeting for a user.
However, she's in love with Johnny, and would like to greet him slightly different.
She added a special case to her function, but she made a mistake.

def greet(name):
    return "Hello, {name}!".format(name=name)
    if name == "Johnny":
        return "Hello, my love!"
"""
# my solution
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


# II. Simple: Find The Distance Between Two Points
"""
DESCRIPTION:
Given two ordered pairs calculate the distance between them.
Round to two decimal places.
This should be easy to do in 0(1) timing.

def distance(x1, y1, x2, y2):
    # Your code here
"""
# my solution
def distance(x1, y1, x2, y2):
  # Calculate the difference in x and y coordinates
  dx = x2 - x1
  dy = y2 - y1

  # Apply the distance formula and round to two decimal places
  return round(((dx ** 2) + (dy ** 2)) ** 0.5, 2)


# III. No yelling!
"""
Write a function taking in a string like "WOW this is REALLY          amazing"
 and returning "Wow this is really amazing".
String should be capitalized and properly spaced.
Using re and string is not allowed.

def filter_words(st):
    pass
"""
# my solution
def filter_words(st):
    words = st.split()
    new_st = " ".join(words).lower().capitalize()
    return new_st


# IV. Convert a Number to a String
# We need a function that can transform a number (integer) into a string.
def number_to_string(num):
    return str(num)


# V. Reversing Words in a String
"""
Description:
You need to write a function that reverses the words in a given string.
A word can also fit an empty string. If this is not clear enough, here are some examples:
As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
"""
# my solution
def reverse(st):
    words = st.split()
    words.reverse()
    return " ".join(words)


# VI. Reverse List Order
"""
Description:
In this kata you will create a function that takes in a list and returns a list with the reverse order.

def reverse_list(l):
  return a list with the reverse order of l
"""
# my solution
def reverse_list(l):
    new_list = list(reversed(l))
    return new_list

# VII. Multiples of 3 or 5
"""
Description:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0.
Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(number):
    pass
"""
# my solution
def solution(number):
    return sum(x for x in range(1, number) if x % 3 == 0 or x % 5 == 0)


# VIII. Will you make it?
"""
Description:
You were camping with your friends far away from home, but when it's time to go back, \
you realize that your fuel is running out and the nearest pump is 50 miles away!\
You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.

Considering these factors, write a function that tells you if it is possible to get to the pump or not.
Function should return true if it is possible and false if not.

def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
"""
# my solution
def zeroFuel(distance_to_pump, mpg, fuel_left):
    return mpg*fuel_left >= distance_to_pump


# IX. Are You Playing Banjo?
"""
Description:
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

def are_you_playing_banjo(name):
    # Implement me!
    return name
"""
# my solution
def are_you_playing_banjo(name):
  if name[0].lower() == "r":
    return f"{name} plays banjo"
  else:
    return f"{name} does not play banjo"


# IX. Are You Playing Banjo?
"""
Description:
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo" 
name + " does not play banjo"
"""
# my solution
def are_you_playing_banjo(name):
    return f'{name} {"plays banjo" if name[0].lower() == "r" else "does not play banjo"}'


# X. Convert boolean values to strings 'Yes' or 'No’
"""
Description:
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
"""
# my solution
def bool_to_word(boolean):
    return "Yes" if boolean else "No"


# XI. Counting sheep
"""
Consider an array/list of sheep where some sheep \
may be missing from their place.
We need a function that counts the number of \
sheep present in the array (true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
"""
# my solution
def count_sheeps(sheep):
    return sum(item for item in sheep if item == True)


# XII. Is this my tail?
"""
Description:
Some new animals have arrived at the zoo. The zoo keeper is concerned 
that perhaps the animals do not have the right tails. To help her, 
you must correct the broken function to make sure that the second 
argument (tail), is the same as the last letter of the 
first argument (body) - otherwise the tail wouldn't fit!

If the tail is right return true, else return false.

The arguments will always be non empty strings, and normal letters.
"""
# my solution
def correct_tail(body, tail):
    return body[-len(tail):] == tail
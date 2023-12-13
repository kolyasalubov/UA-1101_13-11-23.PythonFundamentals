# I. Jenny's secret message
# Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny,
# and would like to greet him slightly different. She added a special case to her function, but she made a mistake.
# Can you help her?
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# II. Find The Distance Between Two Points
# Given two ordered pairs calculate the distance between them. Round to two decimal places.
# This should be easy to do in 0(1) timing.
def distance(x1, y1, x2, y2):
    # Your code here
    resultx = x1 - x2
    resulty = y1 - y2
    result = (resultx ** 2 + resulty ** 2) ** 0.5
    return round(result, 2)

# III. No yelling!
# Write a function taking in a string like WOW this is REALLY          amazing
# and returning Wow this is really amazing.
# String should be capitalized and properly spaced. Using re and string is not allowed.
def filter_words(st):
    result = ''
    st = st.capitalize()
    list_of_string = st.split(' ')
    for i in list_of_string:
        if i:
            result += i + ' '

    return result.lstrip().rstrip()

# IV. Convert a Number to a String
# DESCRIPTION:
# We need a function that can transform a number (integer) into a string.
#
# What ways of achieving this do you know?
#
# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"
def number_to_string(num):
    return str(num)

# V. Reversing Words in a String
#You need to write a function that reverses the words in a given string.
# A word can also fit an empty string. If this is not clear enough, here are some examples:
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
#
# Example (Input --> Output)
#
# "Hello World" --> "World Hello"
# "Hi There." --> "There. Hi"
def reverse(st):
    list = st.split()
    list.reverse()
    result = ' '.join(list)
    return result

# VI. Reverse List Order
#In this kata you will create a function that takes in a list and returns a list with the reverse order.
# Examples (Input -> Output)
# * [1, 2, 3, 4]  -> [4, 3, 2, 1]
# * [9, 2, 0, 7]  -> [7, 0, 2, 9]
def reverse_list(l):
    return l[::-1]

# VII. Multiples of 3 or 5
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
#
# Additionally, if the number is negative, return 0.
#
# Note: If the number is a multiple of both 3 and 5, only count it once.
def solution(number):
    sum = 0
    if number < 0:
        return 0

    for i in range(1, number):
        if i%3 == 0 or i%5 == 0:
            sum += i
    return sum

# VIII. Will you make it?
#You were camping with your friends far away from home, but when it's time to go back,
# you realize that your fuel is running out and the nearest pump is 50 miles away!
# You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.

# Considering these factors, write a function that tells you if it is possible to get to the pump or not.

# Function should return true if it is possible and false if not.
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump/mpg <= fuel_left

# IX. Are You Playing Banjo?
#Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
#
# The function takes a name as its only argument, and returns one of the following strings:
#
# name + " plays banjo"
# name + " does not play banjo"
# Names given are always valid strings.
def are_you_playing_banjo(name):
    # Implement me!
    return name + " plays banjo" if name[0] == 'R' or name[0] == 'r' else name + " does not play banjo"

# X. Convert boolean values to strings 'Yes' or 'No’
#Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'

# XI. Counting sheep
#Consider an array/list of sheep where some sheep may be missing from their place.
#We need a function that counts the number of sheep present in the array (true means present).
#
# For example,
#
# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# The correct answer would be 17.
#
# Hint: Don't forget to check for bad values like null/undefined
def count_sheeps(sheep):
    return sheep.count(True)

# XII. Is this my tail?
# Some new animals have arrived at the zoo.
# The zoo keeper is concerned that perhaps the animals do not have the right tails.
# To help her, you must correct the broken function to make sure that the second argument (tail),
# is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
#
# If the tail is right return true, else return false.
#
# The arguments will always be non empty strings, and normal letters.
def correct_tail(body, tail):
    return True if tail == body[-1] else False
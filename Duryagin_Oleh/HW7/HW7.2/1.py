# Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


# Simple: Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return round(dist, 2)


# No yelling!
def filter_words(st):
    return ' '.join(st.capitalize().split())


# Convert a Number to a String!
def number_to_string(num):
    return str(num)


# Reversing Words in a String
def reverse(st):
    return ' '.join(st.split()[::-1])


# Reverse List Order
def reverse_list(l):
    l.reverse()
    return l


# Multiples of 3 or 5
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


# Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= fuel_left * mpg


# Are You Playing Banjo?
def areYouPlayingBanjo(name):
    return name + (' plays' if name.lower().startswith('r') else ' does not play') + " banjo"


# Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'


# Counting sheep
def count_sheeps(sheep):
    return sheep.count(True)


# Is this my tail?
def correct_tail(body, tail):
    return body[-1] == tail

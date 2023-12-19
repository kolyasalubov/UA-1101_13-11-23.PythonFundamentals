def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)
"""1"""
def distance(x1, y1, x2, y2):
    result = ((x2-x1)**2 + (y2-y1)**2)**0.5
    result = round(result,2)
    return result
"""2"""
def filter_words(st):
    st = st.lower()
    st = st.capitalize()
    st = " ".join(st.split())
    return st
"""3"""
def number_to_string(num):
    num = str(num)
    return num
"""4"""
def reverse(st):
    st = st.split()[::-1]
    st = " ".join(st)
    return st
"""5"""
def reverse_list(l):
    l =l[::-1]
    return l
"""6"""
def solution(number):
    i = 0
    y = 0
    while i < number:
        if i % 3 == 0 or i % 5 == 0:
            y = y + i
            i += 1
        else:
            i+=1
    return y
"""7"""
def zero_fuel(distance_to_pump, mpg, fuel_left):
    x = distance_to_pump / mpg
    if x <= fuel_left:
        return True
    else:
        return False
"""8"""
def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        name = name + " plays banjo"
    else:
        name = name + " does not play banjo"
    return name
"""9"""
def bool_to_word(boolean):
    if boolean is True:
        return "Yes"
    else:
        return "No"
"""10"""
def count_sheeps(sheep):
    x = sheep.count(True)
    return x
"""11"""
def correct_tail(body, tail):
    x = len(body) - 1
    if body[x] == tail:
        return True
    else:
        return False
"""12"""
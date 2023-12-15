def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"

def distance(x1, y1, x2, y2):
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    distance = round(distance, 2)
    return distance

def filter_words(st):
    st = st.lower().capitalize()
    arr = st.split(" ")
    new_arr = [x for x in arr if x != '']
            
    return " ".join(new_arr)

def number_to_string(num):
    return str(num)

def reverse(st):
    arr = st.split()[::-1]
    return " ".join(arr)

def reverse_list(l):
    return l[::-1]

def solution(number):
    result = 0
    for i in range(number):
        if i%3 == 0 and i%5 == 0:
            result += i
        elif i%3 == 0 or i%5 == 0:
            result += i
            
    return result

def zero_fuel(distance_to_pump, mpg, fuel_left):
    run = distance_to_pump / mpg
    if run == fuel_left or run < fuel_left:
        return True
    else:
        return False
    
def are_you_playing_banjo(name):
    if name[0] in ['r', 'R']:
        return f"{name} plays banjo"
    return f"{name} does not play banjo"

def bool_to_word(boolean):
    return "Yes" if boolean is True else "No"

def count_sheeps(sheep):
    result = 0
    for i in sheep:
        if i:
            result += 1
            
    return result

def correct_tail(body, tail):
    return body[-1] == tail
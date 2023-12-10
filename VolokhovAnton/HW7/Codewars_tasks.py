def greet(name):
    # Returns string "Hello, my love!" only when name is equal to "Johnny"
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"

def distance(x1, y1, x2, y2):
    # Calculate the difference between x-coordinates and y-coordinates
    x_diff = x2 - x1
    y_diff = y2 - y1
    
    # Calculate the distance using the formula: distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    distance = ((x_diff ** 2) + (y_diff ** 2)) ** 0.5
    
    # Round the distance to two decimal places
    rounded_distance = round(distance, 2)
    
    return rounded_distance

def filter_words(st):
    # Split the string into words
    arr = st.split(" ")
    
    # Capitalize the first word and convert the rest to lowercase
    new_arr = [arr[0].capitalize()] + [x.lower() for x in arr[1:] if x != '']

    return " ".join(new_arr)

def number_to_string(num):
    return str(num)

def reverse(st):
    # Split the sentence into words and remove extra spaces
    words = st.split()
    
    # Reverse the order of the words
    reversed_sentence = ' '.join(words[::-1])
    
    return reversed_sentence

def reverse_list(l):
    return l[::-1]

def solution(number):
    result = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            result += i
            
    return result

def zero_fuel(distance_to_pump, mpg, fuel_left):
    # Calculate the distance the car can run with the remaining fuel
    run = fuel_left * mpg
    
    # Check if the calculated distance is enough to reach the pump
    if run >= distance_to_pump:
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
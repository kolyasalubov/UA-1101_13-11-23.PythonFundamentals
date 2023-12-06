# I. Jenny's secret message

def greet(name):
    """
    Function that returns a greeting for a user. And it greats Johnny slightly different.
    """
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


# II. Find The Distance Between Two Points

from math import sqrt


def distance_between_two_points(x1, y1, x2, y2):
    distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(distance, 2)


# III. No yelling!

def filter_words(st):
    """
    Function taking in a string like "WOW this is REALLY          amazing"
    and returning "Wow this is really amazing."
    Output string will be capitalized and properly spaced.
    """
    splited_sentence = st.split()
    new_sentence = ''
    for word in splited_sentence:
        new_sentence = new_sentence + word + ' '
    return new_sentence.capitalize().strip()


# print(filter_words('HELLO CAN YOU HEAR ME')) #=> Hello can you hear me
# print(filter_words('now THIS is REALLY interesting')) #=> Now this is really interesting
# print(filter_words('THAT was EXTRAORDINARY!')) #=> That was extraordinary!


# IV. Convert a Number to a String

def number_to_string(number: int) -> str:
    return str(number)


# print(number_to_string(123))
# print(number_to_string(999))
# print(number_to_string(0))
# print(number_to_string(-248))


# V. Reversing Words in a String

def reverse(st):
    splited_string = st.split()
    splited_string.reverse()
    st = ' '
    for word in splited_string:
        st = st + word + ' '
    return st.strip()

# print(reverse("Hello World"))
# print(reverse("Hi There."))


# VI. Reverse List Order

def reverse_list(input_list):
    input_list.reverse()
    return input_list

# print(reverse_list([1, 2, 3, 4]))


# VII. Multiples of 3 or 5

def solution(number):
    """Return sum of numbers in range of input number that are multiples of 3 o5 5"""
    if number <= 0:
        return 0
    else:
        multiple_list = 0
        for i in range(number):
            if i % 3 == 0 or i % 5 == 0:
                multiple_list += i
        return multiple_list

# print(solution(10))


# VIII. Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    """You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel
    is running out and the nearest pump is 50 miles away! You know that on average, your car runs on
    about 25 miles per gallon. There are 2 gallons left.

    Considering these factors, write a function that tells you if it is possible to get to the pump or not.

    Function should return true if it is possible and false if not."""
    return mpg * fuel_left >= distance_to_pump

# print(zero_fuel(50,30,2))


# IX. Are You Playing Banjo?

def are_you_playing_banjo(name):
    """If your name starts with the letter "R" or lower case "r", you are playing banjo!"""
    if name.lower()[0] == 'r':
        answer = f'{name} plays banjo'
    else:
        answer = f'{name} does not play banjo'
    return answer

# print(are_you_playing_banjo('Ann'))
# print(are_you_playing_banjo('oleg'))
# print(are_you_playing_banjo('Roman'))


# X. Convert boolean values to strings 'Yes' or 'No’

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# print(bool_to_word(True))
# print(bool_to_word(False))

# XI. Counting sheep

def count_sheeps(sheep):
    """Function that counts the number of sheep present in the array (true means present)"""
    # answer = sheep.count(True)
    # return answer
    return sheep.count(True)

# print(count_sheeps([True,  True,  True,  False,
#                   True,  True,  True,  True ,
#                   True,  False, True,  False,
#                   True,  False, False, True ,
#                   True,  True,  True,  True ,
#                   False, False, True,  True]))


# XII. Is this my tail?

def correct_tail(body, tail):
    """
    Function compares if the last letter of 'body' word is the same as 'tail'.
    If the tail is right return true, else return false.
    """
    return body[-1] == tail

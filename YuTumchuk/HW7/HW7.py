#################### Task 1 ######################################

# def largest(number1, number2):
#     """Function returns larger number among two numbers given"""
#     answer = ""
#     if not isinstance(number1, int) or not isinstance(number2, int):
#         print("Please, re-type the numbers.")
#     elif number1 > number2:
#         answer = f"{number1} is larger than {number2}."
#     elif number2 > number1:
#         answer = f"{number2} is larger than {number1}."
#     else:
#         answer = f"{number2} and {number1} are the same!."
#     return answer
#
#
# n1 = int(input("Please, input first number: "))
# n2 = int(input("Please, input second number: "))
#
# print(largest(n1, n2))

#################### Task 2 ######################################
# from math import pi
#
#
# def rectangle_area():
#     dimensions = list(input("Please enter length and width, separated comma: ").split(sep=","))
#     res = int(dimensions[0]) * int(dimensions[1])
#     print(f"The area of rectangle is {res}.")
#
#
# def triangle_area():
#     dimensions = list(input("Please enter base and high, separated comma: ").split(sep=","))
#     res = int(dimensions[0]) * int(dimensions[1]) * 0.5
#     print(f"The area of triangle is {res}.")
#
#
# def circle_area():
#     dimensions = input("Please enter radius: ")
#     res = int(dimensions) ** 2 * pi
#     print(f"The area of circle is {res}.")
#
#
# initial_reguest = input("Write, which figure's area you want to calculate (rectangle, triangle or circle)?")
# if initial_reguest == "rectangle":
#     rectangle_area()
# elif initial_reguest == "triangle":
#     triangle_area()
# elif initial_reguest == "circle":
#     circle_area()
# else:
#     print("You typed something else, please re-run program and type exact name of the figure")

#################### Task 3 ######################################
word = str(input("Write any word: "))
uniqe_symbols=list(set(word))
res = {x:word.count(x) for x in uniqe_symbols}
print(res)

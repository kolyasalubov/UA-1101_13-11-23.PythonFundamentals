import jennySM as jsm
import distance2points as dist
import noYelling as ny
import num2string as n2s
import reverseWords as rw
import reverseListOrder as rlo
import multiples3or5 as m3o5
import willYouMakeIt as wymi
import banjo
import boolean2string as b2s
import countingSheep as cs
import isThisMyTail as tail

print("""
List of tasks:
1. Jenny's secret message
2. Find The Distance Between Two Points
3. No yelling!
4. Convert a Number to a String
5. Reversing Words in a String
6. Reverse List Order
7. Multiples of 3 or 5
8. Will you make it?
9. Are You Playing Banjo?
10. Convert boolean values to strings 'Yes' or 'No'
11. Counting sheep
12. Is this my tail?
      
Enter '0' to exit the program.
""")
user_input = ""
while user_input != "0":
    user_input = input("Enter the number of task you wish to check: ")
    match user_input:
        case "0":
            print("Exiting the program...")
        case "1":
            input_name = input("Enter your name: ")
            print(jsm.greet(input_name))
        case "2":
            x1, y1 = map(int, input("Enter x1, y1: ").strip().split(", "))
            x2, y2 = map(int,input("Enter x2, y2: ").strip().split(", "))
            print(f"{dist.calcDistance(x1, y1, x2, y2):.2f}")
        case "3":
            print(f"Filtered and capitalized sentence: {ny.filter_words(input('Enter your sentence to filter: '))}")
        case "4":
            convertedNumber = n2s.number_to_string(int(input('Enter a number that would be transformed into a string: ')))
            print(f"The transformed number - '{convertedNumber}' and it\'s type is {type(convertedNumber)}.")
        case "5":
            print(f"Reversed sentence: {rw.reverse_f(input("Enter your sentence to reverse: "))}")
        case "6":
            print(f"Reversed list: {rlo.reverse_list(input("Enter your sentence that will be transformed into a list: ").split())}")
        case "7":
            print(f"The sum of multiples of 3 or 5 is: {m3o5.solution(int(input("Enter an upper limit number: ")))}")
        case "8":
            print(f"Will you make it? - {wymi.zero_fuel(float(input("Enter the distance to a gas stationin miles: ")),
            float(input("Enter fuel consumption per mile: ")),
            float(input("Enter the amount of fuel left: ")))}")
        case "9":
            print("If your name starts with 'R' or 'r' - you play banjo.")
            print(f"{banjo.are_you_playing_banjo(input("Enter you name: "))}")
        case "10":
            user_bool = input('Enter \'True\' or \'False\': ')
            if user_bool == "False":
                user_bool = False
            print(f"{b2s.bool_to_word(bool(user_bool))}")
        case "11":
            sheep = list(map(lambda x: False if x == "False" else True, 
                             input("Enter the array of sheep where 'True' represents presence of the sheep \
and 'False' represents it's absence: ").title().split()))
            print(f"The amount of sheep is: {cs.count_sheeps(sheep)}")
            
        case "12":
            print(f"Is this my tail? - {tail.correct_tail(input("Enter the 'body' word: "), input("Enter the 'tail' letter: "))}")
        case _:
            print("Invalid input! Try again.")